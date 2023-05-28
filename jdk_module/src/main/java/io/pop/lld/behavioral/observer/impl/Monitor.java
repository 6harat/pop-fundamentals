package io.pop.lld.behavioral.observer.impl;

import io.pop.lld.behavioral.observer.Event;
import io.pop.lld.behavioral.observer.Publisher;
import io.pop.lld.behavioral.observer.Subscriber;
import io.pop.lld.behavioral.observer.domain.Notification;
import java.util.*;

public class Monitor implements Publisher<Notification> {
  private final Map<String, Set<Subscriber>> subscriptions;

  public Monitor() {
    subscriptions = new HashMap<>();
  }

  @Override
  public void subscribe(final Event event, final Subscriber<Notification> subscriber) {
    Set<Subscriber> eventSubscriptions = subscriptions.get(event.name());
    if (eventSubscriptions == null) {
      eventSubscriptions = new HashSet<>();
      eventSubscriptions.add(subscriber);
      subscriptions.put(event.name(), eventSubscriptions);
      return;
    }

    if (eventSubscriptions.contains(subscriber)) {
      return;
    }

    eventSubscriptions.add(subscriber);
  }

  @Override
  public void unsubscribe(final Event event, final Subscriber<Notification> subscriber) {
    Set<Subscriber> eventSubscriptions = subscriptions.get(event.name());
    if (eventSubscriptions == null || !eventSubscriptions.contains(subscriber)) {
      return;
    }

    eventSubscriptions.remove(subscriber);
  }

  @Override
  public void notify(final Event event, final Notification message) {
    Set<Subscriber> eventSubscriptions = subscriptions.get(event.name());
    if (eventSubscriptions == null) {
      return;
    }

    for (Subscriber<Notification> subscriber : eventSubscriptions) {
      subscriber.onUpdate(event, message);
    }
  }
}
