package io.pop.lld.creational.abstract_factory.impl;

import io.pop.lld.creational.abstract_factory.CourierService;
import io.pop.lld.creational.abstract_factory.CourierServiceFactory;

public class SlowCourierServiceFactory implements CourierServiceFactory {
  @Override
  public CourierService createCourierService(final String type) {
    if ("road".equalsIgnoreCase(type)) {
      return new RoadCourierService(20, 259);
    }
    return null;
  }
}
