package io.pop.lld.behavioral.observer.domain;

public class Notification {
    private final String data;

    public Notification(final String data) {
        this.data = data;
    }

    public String getData() {
        return data;
    }
}
