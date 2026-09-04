with open('c:/nextweb/mandra/site/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('''  .section-partners {
    background: #FFFFFF;
    color: #0B110D;
    padding: 96px 0 110px;
    position: relative;
    overflow: hidden;
    width: 100%;
    border-top: 1px solid rgba(0, 0, 0, 0.06);
  }
  .partners-top-container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 6vw 36px;
  }''', '''  .section-partners {
    background: #FFFFFF;
    color: #0B110D;
    padding: 140px 0 160px;
    min-height: 65vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
    width: 100%;
    border-top: 1px solid rgba(0, 0, 0, 0.06);
  }
  .partners-top-container {
    width: 100%;
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 6vw 50px;
  }''')

with open('c:/nextweb/mandra/site/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('c:/nextweb/mandra/site/numo-style.html', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated padding and min-height')
