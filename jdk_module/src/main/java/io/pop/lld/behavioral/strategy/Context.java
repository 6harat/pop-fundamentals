package io.pop.lld.behavioral.strategy;

public interface Context<Req, Res> {
  void registerStrategy(Search<Req, Res> strategy);
}
