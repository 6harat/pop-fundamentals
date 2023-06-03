package io.pop.lld.creational.abstract_factory;

public interface CourierService {
    int estimateCost(final String source, final String target, final int weight);
    long deliver(final String source, final String target);
}
