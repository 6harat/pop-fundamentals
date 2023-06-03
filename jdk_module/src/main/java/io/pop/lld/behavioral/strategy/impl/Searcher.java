package io.pop.lld.behavioral.strategy.impl;

import io.pop.lld.behavioral.strategy.Context;
import io.pop.lld.behavioral.strategy.Search;
import io.pop.lld.behavioral.strategy.domain.SearchRequest;
import io.pop.lld.behavioral.strategy.domain.SearchResponse;
import java.util.*;

public class Searcher implements Context<SearchRequest, SearchResponse> {
  private final Map<String, Search<SearchRequest, SearchResponse>> strategyMap;

  public Searcher() {
    strategyMap = new HashMap<>();
  }

  public void registerStrategy(final Search<SearchRequest, SearchResponse> strategy) {
    if (strategyMap.containsKey(strategy.name())) {
      return;
    }
    strategyMap.put(strategy.name(), strategy);
  }

  public SearchResponse find(final SearchRequest request) {
    final Search<SearchRequest, SearchResponse> searchStrategy = determineStrategy(request);
    return searchStrategy.execute(request);
  }

  protected Search<SearchRequest, SearchResponse> determineStrategy(final SearchRequest request) {
    if (request.getUser() != null && !request.getUser().isEmpty()) {
      return strategyMap.get("personalized");
    }
    return strategyMap.get("generic");
  }
}
