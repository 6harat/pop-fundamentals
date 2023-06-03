package io.pop.lld.creational.abstract_factory;

public interface CourierServiceAbstractFactory {
    public CourierServiceFactory createFactory(final String factoryType);
}
