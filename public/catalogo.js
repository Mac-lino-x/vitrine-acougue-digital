// CATÁLOGO DE PRODUTOS
// Para trocar uma imagem: substitua o arquivo PNG em /assets/carnes/ mantendo o mesmo nome.
// Para adicionar um produto: coloque o PNG em /assets/carnes/ e acrescente uma linha abaixo.
// unidade: 'kg' | 'duzia' | 'bandeja'

export const UNIDADES = {
  kg:      { label: 'KG',      min: 10, max: 120 },
  duzia:   { label: 'DÚZIA',   min: 4,  max: 30 },
  bandeja: { label: 'BANDEJA', min: 6,  max: 60 }
};

export const CATALOGO = {
  boi: {
    label: 'Boi',
    itens: [
      { nome: 'Picanha',            arquivo: 'picanha.png',          unidade: 'kg' },
      { nome: 'Alcatra',            arquivo: 'alcatra.png',          unidade: 'kg' },
      { nome: 'Contra Filé',        arquivo: 'contra_file.png',      unidade: 'kg' },
      { nome: 'Filé Mignon',        arquivo: 'file_mignon.png',      unidade: 'kg' },
      { nome: 'Maminha',            arquivo: 'maminha.png',          unidade: 'kg' },
      { nome: 'Fraldinha',          arquivo: 'fraldinha.png',        unidade: 'kg' },
      { nome: 'Patinho',            arquivo: 'patinho.png',          unidade: 'kg' },
      { nome: 'Coxão Mole',         arquivo: 'coxao_mole.png',       unidade: 'kg' },
      { nome: 'Coxão Duro',         arquivo: 'coxao_duro.png',       unidade: 'kg' },
      { nome: 'Acém',               arquivo: 'acem.png',             unidade: 'kg' },
      { nome: 'Músculo',            arquivo: 'musculo.png',          unidade: 'kg' },
      { nome: 'Costela de Boi',     arquivo: 'costela_boi.png',      unidade: 'kg' },
      { nome: 'Cupim',              arquivo: 'cupim.png',            unidade: 'kg' },
      { nome: 'Lagarto',            arquivo: 'lagarto.png',          unidade: 'kg' },
      { nome: 'Bife Ancho',         arquivo: 'ancho.png',            unidade: 'kg' },
      { nome: 'Carne Moída de Boi', arquivo: 'carne_moida_boi.png',  unidade: 'kg' },
      { nome: 'Paleta de Boi',      arquivo: 'paleta_boi.png',       unidade: 'kg' },
      { nome: 'Rabo de Boi',        arquivo: 'rabo_boi.png',         unidade: 'kg' },
      { nome: 'Fígado de Boi',      arquivo: 'figado_boi.png',       unidade: 'kg' },
      { nome: 'Hambúrguer',         arquivo: 'hamburguer.png',       unidade: 'kg' }
    ]
  },
  porco: {
    label: 'Porco',
    itens: [
      { nome: 'Bisteca',               arquivo: 'bisteca.png',            unidade: 'kg' },
      { nome: 'Costelinha de Porco',   arquivo: 'costela_porco.png',      unidade: 'kg' },
      { nome: 'Lombo',                 arquivo: 'lombo.png',              unidade: 'kg' },
      { nome: 'Pernil',                arquivo: 'pernil.png',             unidade: 'kg' },
      { nome: 'Paleta de Porco',       arquivo: 'paleta_porco.png',       unidade: 'kg' },
      { nome: 'Panceta',               arquivo: 'panceta.png',            unidade: 'kg' },
      { nome: 'Copa Lombo',            arquivo: 'copa_lombo.png',         unidade: 'kg' },
      { nome: 'Bacon',                 arquivo: 'bacon.png',              unidade: 'kg' },
      { nome: 'Linguiça Toscana',      arquivo: 'linguica_toscana.png',   unidade: 'kg' },
      { nome: 'Linguiça Calabresa',    arquivo: 'linguica_calabresa.png', unidade: 'kg' },
      { nome: 'Joelho de Porco',       arquivo: 'joelho_porco.png',       unidade: 'kg' },
      { nome: 'Carne Moída de Porco',  arquivo: 'carne_moida_porco.png',  unidade: 'kg' }
    ]
  },
  frango: {
    label: 'Frango',
    itens: [
      { nome: 'Peito de Frango',    arquivo: 'peito_frango.png',     unidade: 'kg' },
      { nome: 'Coxa de Frango',     arquivo: 'coxa_frango.png',      unidade: 'kg' },
      { nome: 'Asa de Frango',      arquivo: 'asa_frango.png',       unidade: 'kg' },
      { nome: 'Sobrecoxa',          arquivo: 'sobrecoxa_frango.png', unidade: 'kg' },
      { nome: 'Frango Inteiro',     arquivo: 'frango_inteiro.png',   unidade: 'kg' },
      { nome: 'Coxinha da Asa',     arquivo: 'coxinha_asa.png',      unidade: 'kg' },
      { nome: 'Sassami',            arquivo: 'file_sassami.png',     unidade: 'kg' },
      { nome: 'Moela',              arquivo: 'moela_frango.png',     unidade: 'kg' },
      { nome: 'Coração de Frango',  arquivo: 'coracao_frango.png',   unidade: 'kg' },
      { nome: 'Fígado de Frango',   arquivo: 'figado_frango.png',    unidade: 'kg' },
      { nome: 'Pé de Frango',       arquivo: 'pe_frango.png',        unidade: 'kg' }
    ]
  },
  ovos: {
    label: 'Ovos',
    itens: [
      { nome: 'Ovo Branco',       arquivo: 'ovo_branco.png',   unidade: 'duzia' },
      { nome: 'Ovo Vermelho',     arquivo: 'ovo_vermelho.png', unidade: 'duzia' },
      { nome: 'Ovo Caipira',      arquivo: 'ovo_caipira.png',  unidade: 'duzia' },
      { nome: 'Ovo de Codorna',   arquivo: 'ovo_codorna.png',  unidade: 'bandeja' },
      { nome: 'Bandeja de Ovos',  arquivo: 'bandeja_ovos.png', unidade: 'bandeja' }
    ]
  }
};
