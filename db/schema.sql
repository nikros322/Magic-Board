-- Справочная схема. Основной источник правды — Alembic migration.

CREATE TABLE stories (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL DEFAULT 'Шарль Перро',
    description TEXT,
    audio_url VARCHAR(500),
    cover_url VARCHAR(500),
    map_url VARCHAR(500)
);

CREATE TABLE route_points (
    id SERIAL PRIMARY KEY,
    story_id INTEGER NOT NULL REFERENCES stories(id) ON DELETE CASCADE,
    t INTEGER NOT NULL,
    x INTEGER NOT NULL,
    y INTEGER NOT NULL,
    event VARCHAR(255)
);

CREATE INDEX idx_route_points_story_t ON route_points(story_id, t);
