-- Rules Table
CREATE TABLE rules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rule_string TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- AST Nodes Table
CREATE TABLE ast_nodes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(20) NOT NULL,
    left_node_id INT,
    right_node_id INT,
    value TEXT,
    rule_id INT,
    FOREIGN KEY (left_node_id) REFERENCES ast_nodes(id) ON DELETE CASCADE,
    FOREIGN KEY (right_node_id) REFERENCES ast_nodes(id) ON DELETE CASCADE,
    FOREIGN KEY (rule_id) REFERENCES rules(id) ON DELETE CASCADE
);
