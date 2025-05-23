CREATE TABLE power_plant_v2 (
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE model_metadata (
    id INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    version INTEGER NOT NULL,
    path VARCHAR(1024) NOT NULL,
    features JSONB NOT NULL,
    creation_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    plant_id INTEGER NOT NULL REFERENCES power_plant_v2(id)
);

ALTER TABLE model_metadata
   ADD CONSTRAINT unique_model_version UNIQUE (name, version);
