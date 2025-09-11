# ReposCalebe
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Calebe — Portfólio</title>

  <!-- Fonte moderna — você pode trocar ou remover -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

  <!-- Link para o CSS externo -->
  <link rel="stylesheet" href="ATVV.css">
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a class="logo" href="#home">Portifólio Pessoal<span class="accent">.</span></a>
      <nav class="main-nav" aria-label="Navegação principal">
        <ul>
          <li><a href="#home">Início</a></li>
          <li><a href="#projects">Projetos</a></li>
          <li><a href="#contact">Contato</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main>
    <!-- HERO / PÁGINA INICIAL -->
    <section id="home" class="hero">
      <div class="container hero-grid">
        <div class="hero-text">
          <h1>Calebe Alves</h1>
          <p class="subtitle">Estudante de TI — Analista e Desenvolvedor de Sistemas</p>
          <div class="presentation-card">
  <h2>Sejam Bem Vindos!</h2>
  <p>
    Olá! Meu nome é <strong>Calebe</strong>, tenho 22 anos, nasci em Brasília em uma família humilde...mas rica em amor, uma familia Abençoada e Maravilhosa. Moro ao fundo de uma Oficina Mecânica, meu Pai é Mecânico e minha Mãe é Empregada Domestica.
    Estou cursando TI em <em>ADS (Análise e Desenvolvimento de Sistemas)</em>. Essa é a única matéria em pendência para encerrar esse curso.
    Também estou estudando para concurso público. Atualmente sou Soldado Militar Temporário reengajado da Força Aérea e não tenho mais interesse em continuar; pretendo sair assim que conseguir um emprego na área de TI ou em Concurso Público.
  </p>

  <h3>Meus Hobbys:</h3>
  <ol>
    <li>👥 Rolê com Amigos</li>
    <li>🎮 Games</li>
    <li>⚽ Futebol</li>
    <li>🏋️‍♂️ Academia</li>
    <li>🏎️ Carros</li>
    <li>🍕 Restaurantes / Bares</li>
    <li>🎥 Filmes / Séries</li>
  </ol>

  <p>
    Meu time do coração é o <strong>Cruzeiro 💙</strong>.
  </p>
</div>
          <div class="cta-row">
            <a class="btn btn-primary" href="#projects">Meus Projetos</a>
            <a class="btn btn-outline" href="#contact">Contato</a>
          </div>
        </div>

   <div class="hero-image">
  <img src="https://e7.pngegg.com/pngimages/984/588/png-clipart-undertale-internet-meme-mario-luigi-meme-nintendo-video-game.png" alt="Foto de perfil do Calebe">
</div>
    </section>
    <section id="projects" class="projects">
      <div class="container">
        <header class="section-header">
          <h2>Projetos</h2>
          <p>Alguns projetos e repositórios no GitHub.</p>
        </header>
        <div class="projects-grid">
          <article class="project-card">
            <h3>Projeto — Site Pessoal</h3>
            <p>Portfólio construído com HTML5 e CSS externo. Foco em semântica e responsividade.</p>
            <div class="project-links">
              <a href="https://github.com/SEU_USUARIO/PROJETO2" target="_blank" rel="noopener">Ver repositório</a>
            </div>
          </article>
        </div>
      </div>
    </section>
    <!-- SEÇÃO DE CONTATO -->
    <section id="contact" class="contact">
      <div class="container">
        <header class="section-header">
          <h2>Contato</h2>
          <p>Entre em contato por e-mail ou redes sociais.</p>
        </header>
        <div class="contact-grid">
          <div class="contact-card">
            <h3>Email</h3>
            <p><a href="https://mail.google.com">calebe.santos@sempreceub.com</a></p>
          </div>
          <div class="contact-card">
            <h3>Redes Sociais</h3>
            <ul class="social-list">
              <li><a href="https://github.com/0Calebe0/programacao-web-aula02-Calebe-Alves" target="_blank" rel="noopener">GitHub</a></li>
              <li><a href="https://www.linkedin.com/in/SEU_PERFIL" target="_blank" rel="noopener">LinkedIn</a></li>
              <li><a href="https://www.instagram.com/calebeealvess/" target="_blank" rel="noopener">Instagram</a></li>
            </ul>
          </div>
          <div class="contact-card contact-form-card">
            <h3>Mensagem rápida</h3>
            <!-- Formulário simples que envia por email (mailto) ou pode ser substituído por backend -->
            <form action="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new" method="post" enctype="text/plain">
              <label for="name">Nome</label>
              <input id="name" name="name" type="text" placeholder="Seu nome">
              <label for="message">Mensagem</label>
              <textarea id="message" name="message" rows="4" placeholder="Escreva uma mensagem..."></textarea>
              <button class="btn btn-primary" type="submit">Enviar</button>
            </form>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-inner">
      <p>&copy; <span id="year"></span> Calebe Alves. Todos os direitos reservados.</p>
      <nav aria-label="Rodapé">
        <ul>
          <li><a href="#home">Início</a></li>
          <li><a href="#projects">Projetos</a></li>
          <li><a href="#contact">Contato</a></li>
        </ul>
      </nav>
    </div>
  </footer>

  <script>
    // Atualiza o ano automaticamente
    document.getElementById('year').textContent = new Date().getFullYear();
  </script>
</body>
</html>
