package io.pop.lld.behavioral.iterator.impl;

import io.pop.lld.behavioral.iterator.Iterable;
import io.pop.lld.behavioral.iterator.Iterator;

public class Matrix<T> implements Iterable<T> {
    private final T[][] elements;
    private final int rowSize;
    private final int colSize;

    public Matrix(final T[][] elements, final int rowSize, final int colSize) {
        this.elements = elements;
        this.rowSize = rowSize;
        this.colSize = colSize;
    }

    public int getRowSize() {
        return rowSize;
    }

    public int getColSize() {
        return colSize;
    }

    public T getElement(final int rowIdx, final int colIdx) {
        return elements[rowIdx][colIdx];
    }

    @Override
    public Iterator<T> iterator() {
        return new RowWiseMatrixIterator(this);
    }
}
