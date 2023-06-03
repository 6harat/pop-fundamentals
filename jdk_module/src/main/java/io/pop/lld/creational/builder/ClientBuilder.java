package io.pop.lld.creational.builder;

public interface ClientBuilder {
  Client build();

  void reset();

  void setTarget();

  void setPoolSize();
}
