package io.pop.lld.creational.prototype.impl;

import io.pop.lld.creational.prototype.Project;

public class GrpcMicroserviceProject extends MicroserviceProject {
    @Override
    public void createServer() {
        System.out.println("grpc server created");
    }

    @Override
    public void defineAPIs() {
        System.out.println("grpc APIs defined");
    }

    @Override
    public void configureValidation() {
        System.out.println("grpc validation configured");
    }
}
