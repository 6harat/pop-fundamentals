package io.pop.lld.creational.abstract_factory.impl;

import io.pop.lld.creational.abstract_factory.CourierServiceAbstractFactory;
import io.pop.lld.creational.abstract_factory.CourierServiceFactory;

public class CourierServiceFactoryProvider implements CourierServiceAbstractFactory {
  @Override
  public CourierServiceFactory createFactory(final String factoryType) {
    if ("fast".equalsIgnoreCase(factoryType)) {
      return new FastCourierServiceFactory();
    }
    return new SlowCourierServiceFactory();
  }
}
