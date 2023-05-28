package io.pop.lld.behavioral.observer.impl;

import io.pop.lld.behavioral.observer.Event;
import io.pop.lld.behavioral.observer.Subscriber;
import io.pop.lld.behavioral.observer.domain.Notification;

public class EmailNotifier implements Subscriber<Notification> {

    @Override
    public void onUpdate(Event event, Notification notification) {
        System.out.println("notified on email: " + notification.getData());
    }
}