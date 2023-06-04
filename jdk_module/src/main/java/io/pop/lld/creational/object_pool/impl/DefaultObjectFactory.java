package io.pop.lld.creational.object_pool.impl;

import io.pop.lld.creational.object_pool.ObjectFactory;
import io.pop.lld.creational.object_pool.domain.Client;

public class DefaultObjectFactory implements ObjectFactory<Client> {
  private final String target;

  public DefaultObjectFactory(final String target) {
    this.target = target;
  }

  @Override
  public Client createObject() {
    return new Client(target);
  }
}
