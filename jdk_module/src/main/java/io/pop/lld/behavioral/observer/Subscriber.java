package io.pop.lld.behavioral.observer;

public interface Subscriber<N> {
  void onUpdate(final Event event, final N notification);
}
