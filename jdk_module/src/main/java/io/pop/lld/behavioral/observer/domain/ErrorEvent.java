package io.pop.lld.behavioral.observer.domain;

import io.pop.lld.behavioral.observer.Event;

public class ErrorEvent implements Event {
    private static final String NAME = "error";

    public String name() {
        return NAME;
    }
}
