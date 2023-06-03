package io.pop.lld.behavioral.strategy.impl;

import io.pop.lld.behavioral.strategy.Search;
import io.pop.lld.behavioral.strategy.domain.SearchRequest;
import io.pop.lld.behavioral.strategy.domain.SearchResponse;
import java.util.*;

public class PersonalizedSearch implements Search<SearchRequest, SearchResponse> {
  private static final String NAME = "personalized";

  @Override
  public String name() {
    return NAME;
  }

  @Override
  public SearchResponse execute(final SearchRequest request) {
    System.out.println("received request: " + request);
    return new SearchResponse(List.of("foo", "bar"));
  }
}
