-- =========================================
-- WeddingRent
-- Этап 18. Создание таблицы свадебных нарядов
-- =========================================

CREATE TABLE dresses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    size VARCHAR(20) NOT NULL,
    rental_price NUMERIC(10, 2) NOT NULL
        CHECK (rental_price >= 0),
    deposit_amount NUMERIC(10, 2) NOT NULL
        CHECK (deposit_amount >= 0),
    status VARCHAR(30) NOT NULL DEFAULT 'available'
        CHECK (status IN ('available', 'rented', 'maintenance')),
    condition_description TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_dresses_status
    ON dresses(status);

CREATE INDEX idx_dresses_size
    ON dresses(size);