package io.pop.lld.behavioral.chain_of_responsibility.domain;

public class Request {
  private final String user;
  private final String query;

  public Request(final String user, final String query) {
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
