package io.pop.lld.behavioral.observer;

public interface Publisher<N> {
  void subscribe(final Event event, final Subscriber<N> subscriber);

  void unsubscribe(final Event event, final Subscriber<N> subscriber);

  void notify(final Event event, final N message);
}
