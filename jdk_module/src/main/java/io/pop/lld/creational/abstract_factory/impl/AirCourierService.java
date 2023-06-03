package io.pop.lld.creational.abstract_factory.impl;

import io.pop.lld.creational.abstract_factory.CourierService;

public class AirCourierService implements CourierService {
  private final int baseCost;
  private final long duration;

  public AirCourierService(final int baseCost, final long duration) {
    this.baseCost = baseCost;
    this.duration = duration;
  }

  @Override
  public int estimateCost(final String source, final String target, final int weight) {
    return baseCost + weight * 300;
  }

  @Override
  public long deliver(final String source, final String target) {
    System.out.println("delivered package form " + source + " to " + target);
    return duration;
  }
}
