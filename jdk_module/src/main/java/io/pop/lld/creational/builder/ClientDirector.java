package io.pop.lld.creational.builder;

public class ClientDirector {
  private ClientBuilder builder;

  public ClientDirector(final ClientBuilder builder) {
    this.builder = builder;
  }

  public Client createClient() {
    builder.setPoolSize();
    builder.setTarget();
    return builder.build();
  }
}
