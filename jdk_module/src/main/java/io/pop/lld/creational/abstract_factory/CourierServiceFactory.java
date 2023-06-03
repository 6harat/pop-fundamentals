package io.pop.lld.creational.abstract_factory;

public interface CourierServiceFactory {
    CourierService createCourierService(final String type);
}
