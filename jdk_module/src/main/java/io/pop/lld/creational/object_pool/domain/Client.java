package io.pop.lld.creational.object_pool.domain;

public class Client {
  private String target;

  public Client(final String target) {
    this.target = target;
  }

  public String execute(final String query) {
    return query + " result from " + target;
  }
}
