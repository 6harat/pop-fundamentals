package io.pop.lld.behavioral.strategy.domain;

public class SearchRequest {
    private final String user;
    private final String query;

    public SearchRequest(final String user, final String query) {
        this.user = user;
        this.query = query;
    }

    public String getUser() {
        return user;
    }

    public String getQuery() {
        return query;
    }
}
