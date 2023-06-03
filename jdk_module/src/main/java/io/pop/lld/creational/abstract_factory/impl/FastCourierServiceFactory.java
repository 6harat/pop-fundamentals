package io.pop.lld.creational.abstract_factory.impl;

import io.pop.lld.creational.abstract_factory.CourierService;
import io.pop.lld.creational.abstract_factory.CourierServiceFactory;

public class FastCourierServiceFactory implements CourierServiceFactory {
    @Override
    public CourierService createCourierService(final String type) {
        if ("air".equalsIgnoreCase(type)) {
            return new AirCourierService(100, 78);
        }
        return null;
    }
}
