package io.pop.lld.behavioral.chain_of_responsibility.domain;

public class Response {
  private String result;
  private String error;

  public String getResult() {
    return result;
  }

  public void setResult(final String result) {
    this.result = result;
  }

  public String getError() {
    return error;
  }

  public void setError(final String error) {
    this.error = error;
  }
}
