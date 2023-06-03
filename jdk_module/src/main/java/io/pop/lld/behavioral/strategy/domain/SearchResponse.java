package io.pop.lld.behavioral.strategy.domain;

import java.util.*;

public class SearchResponse {
    private List<String> matches;

    public SearchResponse(List<String> matches) {
        this.matches = matches;
    }

    public List<String> getMatches() {
        return matches;
    }
}
