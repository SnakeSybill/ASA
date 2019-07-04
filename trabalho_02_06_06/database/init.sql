CREATE TABLE tb_categorias 
            (id_categoria SERIAL PRIMARY KEY, 
            tituloCategoria VARCHAR(60),
            descricaoCategoria VARCHAR(200),
            fg_ativo INT default 1);

CREATE TABLE tb_fornecedores 
            (id_fornecedor SERIAL PRIMARY KEY, 
            cnpj VARCHAR(60),
            razaoSocial VARCHAR(200),
            telefone VARCHAR(60),
            contato VARCHAR(60),
            endereco varchar(100),
            fg_ativo INT default 1);

CREATE TABLE tb_produtos 
            (id_produto SERIAL PRIMARY KEY, 
            id_fornecedor INT references tb_fornecedores(id_fornecedor) NOT NULL, 
            id_categoria INT references tb_categorias(id_categoria) NOT NULL, 
            nomeProduto VARCHAR(60),
            descricaoProduto VARCHAR(200),
            valorUnitario NUMERIC,
            quantidade INT,
            quantidadeMinima INT,
            fg_ativo INT default 1);

CREATE TABLE tb_vendedores 
            (id_vendedor SERIAL PRIMARY KEY, 
            cpf VARCHAR(60),
            nome VARCHAR(200),
            telefone VARCHAR(60),
            carteiraTrabalho VARCHAR(60),
            dataAdmissao timestamp,
            fg_ativo INT default 1);

CREATE TABLE tb_vendas 
            (id_venda SERIAL PRIMARY KEY, 
            id_produto INT references tb_produtos(id_produto) NOT NULL,
            id_vendedor INT references tb_vendedores(id_vendedor) NOT NULL, 
            id_categoria INT references tb_categorias(id_categoria) NOT NULL, 
            dataVenda timestamp,
            valorTotal NUMERIC,
            quantidade INT,
            fg_ativo INT default 1);

CREATE TABLE tb_compras 
            (id_compra SERIAL PRIMARY KEY, 
            id_produto INT references tb_produtos(id_produto) NOT NULL,
            id_fornecedor INT references tb_fornecedores(id_fornecedor) NOT NULL, 
            id_categoria INT references tb_categorias(id_categoria) NOT NULL, 
            dataCompra timestamp,
            valorTotal NUMERIC,
            quantidade INT,
            fg_ativo INT default 1);

INSERT INTO tb_categorias (tituloCategoria, descricaoCategoria) VALUES ('Frutas', 'Frutas Saudáveis');
INSERT INTO tb_categorias (tituloCategoria, descricaoCategoria) VALUES ('Eletrônicos', 'Aparelhos Eletrônicos');

INSERT INTO tb_fornecedores (cnpj, razaoSocial, telefone, endereco, contato) VALUES ('51.857.641/0001-06', 'Sacolão Center', '3249-9845', 'Rua das Frutas', 'sacolao@apple.com.br');
INSERT INTO tb_fornecedores (cnpj, razaoSocial, telefone, endereco, contato) VALUES ('15.491.572/0001-98', 'Eletronix', '3654-7596', 'Rua Santana', 'eletronix@gmail.com');

INSERT INTO tb_produtos (id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima) VALUES (1, 1, 'Maçã', 'Maçã Fuji', 1, 10, 1);
INSERT INTO tb_produtos (id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima) VALUES (1, 1, 'Banana', 'Banana Prata', 1, 40, 4);
INSERT INTO tb_produtos (id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima) VALUES (1, 1, 'Ameixa', 'Ameixa Nacional', 12, 20, 1);

INSERT INTO tb_produtos (id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima) VALUES (2, 2, 'Arduino', 'Arduino Nano', 100, 10, 1);
INSERT INTO tb_produtos (id_fornecedor, id_categoria, nomeProduto, descricaoProduto, valorUnitario, quantidade, quantidadeMinima) VALUES (2, 2, 'Raspberry Pi 3', 'Modelo B+ Anatel', 270, 5, 1);
