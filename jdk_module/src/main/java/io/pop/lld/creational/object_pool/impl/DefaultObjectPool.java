package io.pop.lld.creational.object_pool.impl;

import io.pop.lld.creational.object_pool.ObjectFactory;
import io.pop.lld.creational.object_pool.ObjectPool;
import io.pop.lld.creational.object_pool.domain.Client;
import java.util.*;

public class DefaultObjectPool implements ObjectPool<Client> {
  private final int maxPoolSize;
  private final ObjectFactory<Client> objectFactory;
  private final List<Client> activePool;
  private final List<Client> inactivePool;

  public DefaultObjectPool(final int maxPoolSize, final ObjectFactory<Client> objectFactory) {
    this.maxPoolSize = maxPoolSize;
    this.objectFactory = objectFactory;
    activePool = new ArrayList<>(maxPoolSize);
    inactivePool = new ArrayList<>(maxPoolSize);
  }

  @Override
  public int getMaxPoolSize() {
    return maxPoolSize;
  }

  @Override
  public ObjectFactory<Client> getObjectFactory() {
    return objectFactory;
  }

  @Override
  public synchronized Optional<Client> acquire() {
    int iSize = inactivePool.size();
    if (iSize > 0) {
      final Client client = inactivePool.remove(iSize - 1);
      activePool.add(client);
      return Optional.of(client);
    }

    if (activePool.size() >= maxPoolSize) {
      return Optional.empty();
    }

    final Client client = objectFactory.createObject();
    activePool.add(client);
    return Optional.of(client);
  }

  @Override
  public synchronized void release(final Client client) {
    inactivePool.add(client);
  }
}
