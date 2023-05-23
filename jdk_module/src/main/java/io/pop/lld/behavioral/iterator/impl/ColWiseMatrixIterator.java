package io.pop.lld.behavioral.iterator.impl;

import io.pop.lld.behavioral.iterator.Iterator;
import io.pop.lld.behavioral.iterator.NoSuchElementException;

public class ColWiseMatrixIterator<T> implements Iterator<T> {
    private final Matrix<T> matrix;
    private int rowIdx = 0;
    private int colIdx = 0;
    
    public ColWiseMatrixIterator(final Matrix<T> matrix) {
        this.matrix = matrix;
    }

    @Override
    public T next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }

        T element = matrix.getElement(rowIdx, colIdx);
        rowIdx++;
        if (rowIdx == matrix.getRowSize()) {
            rowIdx %= matrix.getRowSize();
            colIdx++;
        }
        return element;
    }

    @Override
    public boolean hasNext() {
        return matrix != null && colIdx < matrix.getColSize();
    }
}
