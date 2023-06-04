package io.pop.lld.creational.prototype.impl;

import io.pop.lld.creational.prototype.Project;

public abstract class MicroserviceProject implements Project {
    protected abstract void createServer();
    protected abstract void defineAPIs();
    protected abstract void configureValidation();

    @Override
    public void create() {
        createServer();
        defineAPIs();
        configureValidation();
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return super.clone();
    }    
}
