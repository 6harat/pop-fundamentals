package io.pop.lld.behavioral.observer.impl;

import io.pop.lld.behavioral.observer.Event;
import io.pop.lld.behavioral.observer.Subscriber;
import io.pop.lld.behavioral.observer.domain.Notification;

public class SlackNotifier implements Subscriber<Notification> {
  @Override
  public void onUpdate(Event event, Notification notification) {
    if (!"error".equalsIgnoreCase(event.name())) {
      return;
    }
    System.out.println("notified on slack: " + notification.getData());
  }
}
