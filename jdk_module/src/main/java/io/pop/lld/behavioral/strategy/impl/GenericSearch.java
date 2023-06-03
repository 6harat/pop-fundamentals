package io.pop.lld.behavioral.strategy.impl;

import io.pop.lld.behavioral.strategy.Search;
import io.pop.lld.behavioral.strategy.domain.SearchRequest;
import io.pop.lld.behavioral.strategy.domain.SearchResponse;
import java.util.*;

public class GenericSearch implements Search<SearchRequest, SearchResponse> {
    private static final String NAME = "generic";

    @Override
    public String name() {
        return NAME;
    }

    @Override
    public SearchResponse execute(final SearchRequest request) {
        System.out.println("recevied request: " + request);
        return new SearchResponse(List.of("hello", "world"));
    }

}
