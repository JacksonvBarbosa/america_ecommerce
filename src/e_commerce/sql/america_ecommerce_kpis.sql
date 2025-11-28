-- Por cause do hifen(-) é necessário inserir aspas duplas ao chamar o schema
SELECT * FROM "e-commerce".ecommerce_america LIMIT 10;

-- Análises de Dados:

-- Ticket Médio das Vendas
SELECT
	ROUND(CAST(SUM(sales) / COUNT(*) AS numeric), 2) AS ticket_medio
FROM 	"e-commerce".ecommerce_america;

-- Taxa de desconto médio das vendas:
SELECT
 	(ROUND(CAST(SUM(discount) / COUNT(*) AS numeric), 1) * 10) AS desconto_medio_porcentagem
FROM "e-commerce".ecommerce_america;

-- Volume de vendas no ano
SELECT
	SUM(quantity) AS qtde_vendidas
FROM "e-commerce".ecommerce_america;

-- Total de Vendas por mês no ano
SELECT
	DATE_TRUNC('month', order_date::timestamp) AS mes,
	SUM(sales) AS total_de_vendas
FROM "e-commerce".ecommerce_america
GROUP BY DATE_TRUNC('month', order_date::timestamp)
ORDER BY mes;

-- Tabela de vendas por dia no mês
SELECT
	DATE_TRUNC('day', order_date::timestamp) AS dia_mes,
	SUM(sales) AS total_de_vendas
FROM "e-commerce".ecommerce_america
GROUP BY DATE_TRUNC('day', order_date::timestamp)
ORDER BY dia_mes;

-- Top 10 produtos por faturamento bruto
-- Caso queira forçar o cifrão na frente do resultado insir antes do to_char 'R$' ou 'S' || ....
SELECT
	product AS produto,
	to_char(SUM(gross_revenue), 'L999G999G999G990') AS faturamento_bruto
FROM "e-commerce".ecommerce_america
GROUP BY product
ORDER BY faturamento_bruto DESC;

-- Top categorias por faturamento bruto
-- Caso queira forçar o cifrão na frente do resultado insir antes do to_char 'R$' ou 'S' || ....
SELECT
	product_category AS categoria_do_produto,
	to_char(SUM(gross_revenue), 'L999G999G999G990') AS faturamento_bruto
FROM "e-commerce".ecommerce_america
GROUP BY product_category
ORDER BY faturamento_bruto DESC;

-- Top 10 produtos por lucro obtido
-- Caso queira forçar o cifrão na frente do resultado insir antes do to_char 'R$' ou 'S' || ....
SELECT
	product AS produto,
	'$' || to_char(SUM(profit), '999,999,999,990.99') AS lucro_por_produto
FROM "e-commerce".ecommerce_america
GROUP BY product
ORDER BY lucro_por_produto DESC;

-- Top categorias por lucro obtido
-- Caso queira forçar o cifrão na frente do resultado insir antes do to_char 'R$' ou 'S' || ....
SELECT
	product_category AS categoria_do_produto,
	'$' || to_char(SUM(profit), '999,999,999,990.99') AS lucro_por_categoria
FROM "e-commerce".ecommerce_america
GROUP BY product_category
ORDER BY lucro_por_categoria DESC;

-- Margem Média de lucro por produto
SELECT
    product,
    ROUND( AVG(profit / sales)::numeric * 100, 1 ) AS margem_lucro_media
FROM "e-commerce".ecommerce_america
GROUP BY product
ORDER BY margem_lucro_media DESC;

-- Forma de pagamento quantidade
SELECT
	payment_method,
	COUNT(payment_method) AS qtde_metodo_pagamento
FROM "e-commerce".ecommerce_america
GROUP BY payment_method
ORDER BY qtde_metodo_pagamento DESC;

