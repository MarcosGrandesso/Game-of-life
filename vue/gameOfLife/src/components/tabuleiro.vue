<div id="game">
  <template v-for="linha in linhas">
      <div v-for = "coluna in colunas" :style="{
              width: tamanho + 'px',
              height: tamanho + 'px',
              background: '#ccc',
              border: '1px solid #eee',
              position: 'absolute',
              top: linha * tamanho,
              left: coluna * tamanho,
      }"></div>
  </template>
  <div v-for="bloco in blocos" :style="{
      width: tamanho + 'px',
      height: tamanho + 'px',
      background: '#666',
      border: '1px solid #eee',
      position: 'absolute',
      top: bloco.y * tamanho,
      left: bloco.x * tamanho,
}"></div>
</div>
<script src="https://unpkg.com/vue@next"></script>
<script>
Vue.createApp({
  data: () => ({
      linhas: 20,
      colunas: 20,
      tamanho: 20,
      blocos: [{ x: 2, y: 4 },{ x: 1, y: 4 }],
      tempo: 1000 / 5,
      direcao: 'direita'
  }),
  mounted (){ //chamar a função mounted que vai executar assim que o vue executar o game
      window.addEventListener("keydown", (event) => {
          console.log(event.which);
      })
      setInterval(() => {
          var x = this.blocos[0].x
          var y = this.blocos[0].y
          if (this.direcao == 'direita') { // se o a direção é a direita eu adicono um bloco para a direita
              x = (x + 1) > this.colunas ? x = 1 : x + 1
          }
          this.blocos.unshift({x, y})
          this.blocos.pop() // aqui a gente está removendo o último item
      }, this.tempo)
  }
}).mount("#game")
</script>