# Otimização da prévia

As quatro imagens originais somavam 709.647 bytes. As versões WebP maiores utilizadas pela página somam 129.498 bytes: redução de 81,8%. Essa comparação mede tamanho de arquivos, não tempo de carregamento.

- Imagens com `srcset` e `sizes`, para o navegador escolher a resolução adequada.
- Foto principal com prioridade alta; imagens das demais seções com carregamento sob demanda.
- Dimensões explícitas nas imagens e decodificação assíncrona.
- Logo original reenquadrada e reduzida de 105.204 para 8.566 bytes.
- Fontes WOFF2 locais, com licenças em `assets/fonts/`, troca sem bloquear o texto e pré-carregamento das fontes iniciais.
- JavaScript sem bibliotecas e carregado com `defer`.
- Menu móvel com fechamento ao escolher uma seção, clicar fora ou pressionar Escape.

Validação: referências locais, âncoras internas, dimensões e textos alternativos das imagens; sintaxe JavaScript; conferência no navegador em celular e computador. Comparativo de cabos e navegação móvel conferidos.

Os originais foram preservados em `assets/` e não são carregados pelo HTML. Para regenerar as imagens, execute `python optimize-images.py` com Pillow disponível. A pasta `.tools/` contém apenas ferramentas locais e está ignorada pelo Git.
