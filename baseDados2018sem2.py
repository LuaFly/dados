import xlrd
import csv

arquivo = "baseDados2018sem2.xlsx"

born =0

ra_comparar=0

vinte = 0
atetrinta = 0
atequart = 0
maisquart = 0

s_masc = 0
s_fem  = 0

c_branco = 0
c_pardo = 0
c_amarelo = 0
c_preto = 0
c_outro = 0

r_catolico = 0
r_ateu = 0
r_evangelica = 0
r_agnostico = 0
r_espirita = 0
r_outros = 0

ec_solteiro = 0
ec_casado = 0
ec_outros = 0

t_deficiencia = 0
deficiencia_aud = 0
deficiencia_fala = 0
deficiencia_visu = 0
deficiencia_outros = 0

t_filhos= 0
um_filho = 0
dois_filhos = 0
tresoumais = 0

t_fora_a_escolha = 0
n_trabalhei = 0
t_area_escolha = 0
t_desempregado = 0

p_t_m_t = 0
p_t_r_t = 0
p_t_n=0
p_t_mout = 0
cuzao = 0

e_sp = 0
e_mg =0

m_fran = 0
m_rest = 0
m_ipua = 0
m_outro = 0

imo_ced = 0
imo_pro = 0
imo_fin = 0
imo_alug = 0

atedez = 0
atevinte = 0
maisvinte = 0

mora_com_familia = 0
mora_com_comp=0
mora_com_famcomp = 0
mora_outros = 0

tot_pessum = 0
tot_pessquat = 0
tot_pessixmais = 0

pes_remune= 0
duas_remune = 0
tres_remune = 0
quat_remune = 0

um_pc = 0
dois_pc = 0
tres_pc = 0
no_pc=0

moto = 0
carro = 0
onibus = 0
outro_loc= 0

um_salario = 0
dois_sm = 0
tres_sm = 0
quatro_sm = 0
cinco_sm = 0
acima_cinco = 0

manha=0
noite=0

int_public = 0
int_particular = 0
maior_public = 0
int_partic = 0

conhece_info = 0
not_info = 0
inv_info = 0

word = 0
excel =0
windows = 0
outros_app1 = 0
outros_app2 = 0
outros_app3 = 0
outros_app4 = 0
outros_app5 = 0
outros_app6 = 0
inv_app = 0

ingles = 0
ing_ale=0
ing_it = 0
ing_esp=0
esp=0
no_idioma = 0

estud_escola = 0
not_estud = 0
babaca= 0
ads=0
gpi=0
ads_inv=0

ano_fatec =0
ano_dois =0

indicacao=0
qualidade=0
graduacao=0
outros_mot=0

tabela = xlrd.open_workbook(arquivo).sheet_by_index(0)
qtd_linhas = tabela.nrows
linhas = []

def tem_palavra(palavras, frase):
    for i in range(0,len(palavras)):
        if str(palavras[i]) in str(frase):
            return True
    return False

def existe_ra(ra_comparar,lista):
    for i in range(0,len(lista)-1):
        if lista[i]['Ra']==ra_comparar:
            return True
    return False

for i in range(1, qtd_linhas):
    linhas.append(
        {
            'Ra': str(tabela.row(i)[3].value), #Fazer
            'nascimento': tabela.row(i)[4].value, 
            'Sexo': tabela.row(i)[5].value,
            'raca': tabela.row(i)[6].value,
            'religiao': tabela.row(i)[7].value,
            'estado_civil': tabela.row(i)[8].value,
            'tem_deficiencia': tabela.row(i)[9].value,
            'deficiencia': tabela.row(i)[10].value,
            'filhos': tabela.row(i)[11].value,
            'trabalho': tabela.row(i)[12].value,
            'periodo_trabalho': tabela.row(i)[13].value,
            'estado': tabela.row(i)[14].value,
            'municipio': tabela.row(i)[15].value,
            'situacao_imovel': tabela.row(i)[18].value,
            'tempo_moradia': tabela.row(i)[19].value, 
            'mora_com': tabela.row(i)[20].value,
            'total_pessoas': tabela.row(i)[21].value,
            'total_pessoas_remuneradas': tabela.row(i)[22].value,
            'computadores': tabela.row(i)[23].value,
            'locomocao': tabela.row(i)[24].value,
            'soma_renda': tabela.row(i)[25].value,
            'periodo_estudo': tabela.row(i)[26].value,
            'vida_escolar': tabela.row(i)[27].value,
            'conhecimentos_info': tabela.row(i)[28].value,
            'aplicativos': tabela.row(i)[29].value,
            'idioma': tabela.row(i)[30].value,
            'estudou_nessa_escola': tabela.row(i)[31].value,
            'qual_curso': tabela.row(i)[32].value,
            'qual_ano': tabela.row(i)[33].value,
            'motivo_vestibular': tabela.row(i)[34].value,
        }
        )

    if existe_ra(linhas[i-1]['Ra'], linhas):
        print ("RA de número {} repetido".format(linhas[i-1]['Ra'][:-2]))
        continue
    
    born = (2018 - int(linhas[i-1]['nascimento'][-4:]))
  
    if born  <= 20:
        vinte = vinte +1
    if born > 20 and  born <=30:
        atetrinta=atetrinta + 1
    if born > 30 and born <=40:
        atequart=atequart+1
    if born >40:
        maisquart = maisquart +1


    if linhas[i-1]['Sexo'] == 'Masculino':
        s_masc=s_masc+1
    else:
        s_fem=s_fem+1
        
    if linhas[i-1]['raca'] == 'Branco':
         c_branco = c_branco+1
    elif linhas[i-1]['raca'] == 'Preto':
         c_preto= c_preto+1
    elif linhas[i-1]['raca'] == 'Pardo':
         c_pardo = c_pardo +1
    elif linhas[i-1]['raca'] == 'Amarelo':
        c_amarelo = c_amarelo +1
    else:
        c_outro = c_outro+1
        
    if linhas[i-1]['religiao'] == 'Católica':
        r_catolico = r_catolico+1
    elif linhas[i-1]['religiao'] == 'Ateu':
        r_ateu = r_ateu+1 
    elif linhas[i-1]['religiao'] == 'Evangélica':
        r_evangelica = r_evangelica+1
    elif linhas[i-1]['religiao'] == 'Agnostico':
        r_agnostico = r_agnostico+1    
    elif linhas[i-1]['religiao'] == 'Espirita':
        r_espirita = r_espirita+1
    else:
        r_outros=r_outros+1
        
    if linhas [i-1] ['estado_civil'] == 'Solteiro':
        ec_solteiro=ec_solteiro+1
    elif linhas [i-1] ['estado_civil'] == 'Casado':
        ec_casado = ec_casado +1
    else:
        ec_outros = ec_outros+1
        
    if linhas[i-1]['tem_deficiencia'] == 'Não':
        t_deficiencia = t_deficiencia +1
    if linhas[i-1]['tem_deficiencia'] == 'Sim':
        if linhas[i-1]['deficiencia'] == 'Auditiva' or linhas[i-1]['deficiencia'] == 'Surdo':
            deficiencia_aud = deficiencia_aud +1
        elif linhas[i-1]['deficiencia'] == 'Fala' or linhas[i-1]['deficiencia'] =='Mudo':
            deficiencia_fala = deficiencia_fala+1
        elif linhas [i-1]['deficiencia'] == 'Visual' or linhas[i-1]['deficiencia'] == 'Cego':
            deficiencia_visu=deficiencia_visu+1
        else:
            deficiencia_outros = deficiencia_outros+1
            
    if linhas [i-1] ['filhos'] == 'Não':
        t_filhos=t_filhos+1
    if linhas [i-1] ['filhos'] == '1 filho':
        um_filho= um_filho+1        
    if linhas [i-1] ['filhos'] == '2 filhos':
        dois_filhos = dois_filhos+1
    if linhas [i-1] ['filhos'] == '3 filhos ou mais':
        tresoumais= tresoumais+1
        
    if linhas [i-1] ['trabalho'] == 'Trabalho fora da área do curso que escolhi':
        t_fora_a_escolha= t_fora_a_escolha +1
    elif linhas [i-1] ['trabalho'] == 'Nunca trabalhei':
        n_trabalhei = n_trabalhei +1
    elif linhas [i-1] ['trabalho'] == 'Trabalho na área do curso que escolhi':
        t_area_escolha =  t_area_escolha +1
    elif linhas [i-1] ['trabalho'] == 'Estou desempregado(a) e nunca trabalhei na área do curso que escolhi':
        t_desempregado = t_desempregado + 1
        
    if linhas [i-1] ['periodo_trabalho'] == 'Manhã e tarde':
        p_t_m_t =p_t_m_t +1
    elif  linhas [i-1] ['periodo_trabalho'] == 'Manhã ou tarde':
        p_t_mout = p_t_mout +1
    elif linhas [i-1] ['periodo_trabalho'] == 'Regime de turnos':
        p_t_r_t = p_t_r_t +1
    elif linhas [i-1] ['periodo_trabalho'] == 'Noite':
        p_t_n = p_t_n +1
    if linhas [i-1] ['trabalho'] == 'Trabalho fora da área do curso que escolhi' and linhas [i-1] ['periodo_trabalho'] == '':
        cuzao = cuzao +1
        
    if linhas [i-1] ['estado'] == 'SP':
        e_sp = e_sp + 1
    if linhas [i-1] ['estado'] == 'MG':
        e_mg = e_mg +1
        
    if linhas [i-1] ['municipio'] == 'Franca':
        m_fran = m_fran + 1
    if linhas [i-1] ['municipio'] == 'Ipuã':
            m_ipua = m_ipua + 1
    if linhas [i-1] ['municipio'] == 'Restinga':
            m_rest = m_rest + 1
    if linhas [i-1] ['municipio'] == 'Outra':
            m_outro = m_outro + 1
            
    if linhas [i-1] ['situacao_imovel'] == 'Cedido':
        imo_ced= imo_ced+1           
    elif linhas [i-1] ['situacao_imovel'] == 'Próprio':
        imo_pro= imo_pro + 1
    elif linhas [i-1] ['situacao_imovel'] == 'Financiado':
        imo_fin= imo_fin +1
    elif linhas [i-1] ['situacao_imovel'] == 'Alugado':
        imo_alug=imo_alug+1

       
    if linhas [i-1] ['tempo_moradia']  <=10:
        atedez=atedez + 1
    if linhas [i-1] ['tempo_moradia']  >10 and linhas [i-1] ['tempo_moradia'] <= 20:
        atevinte=atevinte+1
    if linhas [i-1] ['tempo_moradia']  > 20:
        maisvinte = maisvinte +1
        

    if linhas [i-1] ['mora_com'] == 'Com família (pais e/ou parentes)':
        mora_com_familia = mora_com_familia + 1
    elif linhas [i-1] ['mora_com'] == 'Com o(a) esposa(o), companheiro(a)':
        mora_com_comp=mora_com_comp + 1
    elif linhas [i-1] ['mora_com'] == 'Com a família do(a) esposo(a), companheiro(a)':
        mora_com_famcomp=mora_com_famcomp +1
    else:
        mora_outros = mora_outros +1
        
    if linhas [i-1] ['total_pessoas'] == 'De uma a três':
        tot_pessum = tot_pessum +1
    elif linhas [i-1] ['total_pessoas'] == 'De quatro a seis':
        tot_pessquat = tot_pessquat+1
    elif linhas [i-1] ['total_pessoas'] == 'Mais de seis':
        tot_pessixmais= tot_pessixmais+1

    if linhas[i-1] ['total_pessoas_remuneradas'] == 'Uma':
        pes_remune= pes_remune+1
    elif linhas[i-1] ['total_pessoas_remuneradas'] == 'Duas':
        duas_remune= duas_remune + 1
    elif linhas[i-1] ['total_pessoas_remuneradas'] == 'Três':
        tres_remune= tres_remune+1
    elif linhas[i-1] ['total_pessoas_remuneradas'] == 'Quatro':
        quat_remune = quat_remune + 1

    if linhas [i-1] ['computadores'] == 'Tenho 1':
        um_pc=um_pc+1
    elif linhas [i-1] ['computadores'] == 'Tenho 2':
        dois_pc=dois_pc+1
    elif linhas [i-1] ['computadores'] == 'Tenho 3 ou mais':
        tres_pc=tres_pc+1
    elif linhas [i-1] ['computadores'] == 'Não tenho':
        no_pc = no_pc +1

    if linhas [i-1] ['locomocao'] == 'Moto':
        moto= moto +1
    elif linhas [i-1] ['locomocao'] == 'Carro':
        carro = carro+1
    elif linhas [i-1] ['locomocao'] == 'Ônibus':
        onibus = onibus+1
    else:
        outro_loc = outro_loc +1

    if linhas [i-1] ['soma_renda'] == 'Um salário minimo':
        um_salario = um_salario +1
    elif linhas [i-1] ['soma_renda'] == 'Dois SM':
        dois_sm = dois_sm +1
    elif linhas [i-1] ['soma_renda'] == 'Três SM':
        tres_sm = tres_sm +1
    elif linhas [i-1] ['soma_renda'] == 'Quatro SM':
        quatro_sm = quatro_sm + 1
    elif linhas [i-1] ['soma_renda'] == 'Cinco SM':
        cinco_sm = cinco_sm +1
    elif linhas [i-1] ['soma_renda'] == 'Acima de cinco SM':
        acima_cinco= acima_cinco +1

    if linhas [i-1] ['periodo_estudo'] == 'Manhã':
        manha=manha+1
    elif linhas [i-1] ['periodo_estudo'] == 'Noite':
        noite=noite+1
        
    if linhas [i-1] ['vida_escolar'] == 'Integralmente em escola pública federal, estadual ou municipal':
        int_public = int_public + 1
    if linhas [i-1] ['vida_escolar'] == 'Integralmente em escola particular':
        int_particular = int_particular + 1
    if linhas [i-1] ['vida_escolar'] == 'Maior parte em escola pública':
        maior_public = maior_public+1
    if linhas [i-1] ['vida_escolar'] == 'Maior parte em escola particular':
        int_partic = int_partic +1

    if linhas [i-1] ['conhecimentos_info'] == 'Sim':
        conhece_info = conhece_info + 1
    elif linhas [i-1] ['conhecimentos_info'] == 'Não':
            not_info = not_info + 1
    elif linhas [i-1] ['conhecimentos_info'] == 'Sim, Não':
        inv_info = inv_info + 1
    if linhas [i-1] ['aplicativos'] == 'Word':
            word=word+1
    elif linhas [i-1] ['aplicativos'] == 'Excel':
            excel=excel+1
    elif linhas [i-1] ['aplicativos'] == 'Windows':
            windows = windows +1
    elif linhas [i-1] ['aplicativos'] == 'Excel, Windows':
            outros_app1 = outros_app1 + 1
    elif linhas [i-1] ['aplicativos'] == 'Excel, Windows, Word, Outros':
            outros_app2 = outros_app2 + 1
    elif linhas [i-1] ['aplicativos'] == 'Excel, Windows, Word':
            outros_app3 = outros_app3 + 1
    elif linhas [i-1] ['aplicativos'] == 'Windows, Word, Outros':
            outros_app4 = outros_app4 + 1
    elif linhas [i-1] ['aplicativos'] == 'Excel, Word, Outros':
            outros_app5 = outros_app5 + 1
    elif linhas [i-1] ['aplicativos'] == 'Outros':
            outros_app6 = outros_app6 + 1
    else:
        inv_app=inv_app +1
        
    if linhas [i-1] ['idioma'] == 'Ingles' or linhas [i-1] ['idioma']=='Inglês':
        ingles = ingles +1
    elif linhas [i-1] ['idioma'] == 'Inglês e alemão':
        ing_ale=ing_ale+1
    elif linhas [i-1] ['idioma'] == 'Inglês e Italiano':
        ing_it=ing_it+1
    elif linhas [i-1] ['idioma'] == 'Inglês e espanhol' or linhas [i-1] ['idioma'] == 'Inglês e Espanhol':
        ing_esp= ing_esp+1
    elif linhas [i-1] ['idioma'] == 'Espanhol' or linhas [i-1] ['idioma'] == 'espanhol':
        esp=esp+1
    else:
        no_idioma=no_idioma +1

    if linhas [i-1] ['estudou_nessa_escola'] == 'Sim':
        estud_escola=estud_escola+1
    if linhas [i-1] ['qual_curso'] == 'ADS':
        ads=ads+1
    if linhas [i-1] ['qual_curso'] == 'ADS' and linhas [i-1] ['estudou_nessa_escola'] == 'Não':
        ads_inv=ads_inv+1
    elif linhas [i-1] ['qual_curso'] == 'Gestão da produção industrial':
        gpi=gpi+1
    if linhas [i-1] ['estudou_nessa_escola'] == 'Não':
       not_estud = not_estud+ 1
    if  linhas [i-1] ['estudou_nessa_escola'] == 'Não' and linhas [i-1] ['qual_curso']== 'ADS':
        babaca=babaca+1

    if linhas [i-1] ['qual_ano'] == 2015:
        ano_fatec=ano_fatec+1
    if linhas [i-1] ['qual_ano'] == 2011:
        ano_dois=ano_dois+1

    if tem_palavra(["feedback", "indicação", "amigos", "familiares", "recomendação"], linhas[i-1]['motivo_vestibular']):
        indicacao = indicacao+1
    elif tem_palavra(["faculdade boa", "qualidade", "qualidad", "gratuito", "excelência", "reputação", "estruturado"], linhas[i-1]['motivo_vestibular']):
        qualidade = qualidade+1
    elif tem_palavra(["Adquirir meu primeiro ensino superior", "diploma", "para entrar na área", "por gostar"], linhas[i-1]['motivo_vestibular']):
        graduacao = graduacao+1
    else:
        outros_mot = outros_mot+1

with open('dados.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow('_________idade_____')
    spamwriter.writerow(['Até vinte anos', vinte])
    spamwriter.writerow(['Entre vinte e  trinta', atetrinta])
    spamwriter.writerow(['Entre trinta e quarenta anos', atequart])
    spamwriter.writerow(['Mais de quarenta anos', maisquart])
    spamwriter.writerow('_________Sexo_____')                               
    spamwriter.writerow(['Homens', s_masc])
    spamwriter.writerow(['Mulheres', s_fem])
    spamwriter.writerow('_________Cor_____')                    
    spamwriter.writerow(['Brancos', c_branco])
    spamwriter.writerow(['Negros', c_preto])
    spamwriter.writerow(['Pardos', c_pardo])
    spamwriter.writerow(['Amarelos', c_amarelo])
    spamwriter.writerow(['Outros', c_outro])
    spamwriter.writerow('_________Religiao_____')
    spamwriter.writerow(['Católicos', r_catolico])
    spamwriter.writerow(['Atus', r_ateu])
    spamwriter.writerow(['Evangélicos', r_evangelica])
    spamwriter.writerow(['Agnósticos', r_agnostico])
    spamwriter.writerow(['Espíritas', r_espirita])
    spamwriter.writerow(['Outros', r_outros])
    spamwriter.writerow('_________Estado civil_____')
    spamwriter.writerow(['Solteiros', ec_solteiro])
    spamwriter.writerow(['Casados', ec_casado])
    spamwriter.writerow(['Outros', ec_outros])
    spamwriter.writerow('_________deficiencia_____')
    spamwriter.writerow(['Sem deficiência', t_deficiencia])
    spamwriter.writerow(['Com deficiência auditiva', deficiencia_aud])
    spamwriter.writerow(['Com deficiência visual', deficiencia_visu])
    spamwriter.writerow(['Com deficiência de fala', deficiencia_fala])
    spamwriter.writerow(['Com outros', deficiencia_outros])
    spamwriter.writerow('_________filhos_____')
    spamwriter.writerow(['Sem filhos', t_filhos])
    spamwriter.writerow(['Um filho', um_filho])
    spamwriter.writerow(['Dois filhos', dois_filhos])
    spamwriter.writerow(['Três ou mais filhos', tresoumais])
    spamwriter.writerow('_________trabalha_____')
    spamwriter.writerow(['Nunca trabalharam', n_trabalhei])
    spamwriter.writerow(['Desempregados', t_desempregado])
    spamwriter.writerow(['Trabalham fora da área', t_fora_a_escolha])
    spamwriter.writerow(['Trabalham dentro da área', t_area_escolha])
    spamwriter.writerow('_________periodo que trabalha_____')
    spamwriter.writerow(['Trabalham em período integral', p_t_m_t])
    spamwriter.writerow(['Trabalham meio período (manhã OU tarde)', p_t_mout])
    spamwriter.writerow(['Trabalham em regime de turnos', p_t_r_t])
    spamwriter.writerow(['Trabalham a noite', p_t_n])
    spamwriter.writerow(['Inválido', cuzao])
    spamwriter.writerow('_________Estado_____')
    spamwriter.writerow(['Moram em SP', e_sp])
    spamwriter.writerow(['Moram em MG', e_mg])
    spamwriter.writerow('_________Cidade_____')
    spamwriter.writerow(['Moram em Franca', m_fran])
    spamwriter.writerow(['Moram em Ipuã', m_ipua])
    spamwriter.writerow(['Moram em Restinga', m_rest])
    spamwriter.writerow(['Moram em outro município', m_outro])
    spamwriter.writerow('_________Imovel_____')
    spamwriter.writerow(['Imóvel próprio', imo_pro])
    spamwriter.writerow(['Imóvel alugado', imo_alug])
    spamwriter.writerow(['Imóvel financiado', imo_fin])
    spamwriter.writerow(['Imóvel cedido', imo_ced])
    spamwriter.writerow('_________Tempo de moradia_____')
    spamwriter.writerow(['Até dez anos', atedez])
    spamwriter.writerow(['Até vinte anos', atevinte])
    spamwriter.writerow(['Mais de vinte anos', maisvinte])
    spamwriter.writerow('_________com quem mora_____')                    
    spamwriter.writerow(['Família', mora_com_familia])
    spamwriter.writerow(['Conjulgue', mora_com_comp])
    spamwriter.writerow(['Família do companheiro', mora_com_famcomp])
    spamwriter.writerow(['Outros', mora_outros])
    spamwriter.writerow('_________total pessoas na casa_____')
    spamwriter.writerow(['De uma a tres pessoas', tot_pessum])
    spamwriter.writerow(['De quatro a seis pessoas', tot_pessquat])
    spamwriter.writerow(['Mais de seis pessoas', tot_pessixmais])
    spamwriter.writerow('_________Pessoas remuneradas_____')                   
    spamwriter.writerow(['Uma pessoa trabalha', pes_remune])
    spamwriter.writerow(['Duas pessoas trabalham', duas_remune])
    spamwriter.writerow(['Tres pessoas trabalham', tres_remune])
    spamwriter.writerow(['Quatro pessoas trabalham', quat_remune])
    spamwriter.writerow('_________Computador em casa_____')                    
    spamwriter.writerow(['Sem computador', no_pc])
    spamwriter.writerow(['Um computador', um_pc])
    spamwriter.writerow(['Dois computadores', dois_pc])
    spamwriter.writerow(['Tres ou mais computadores', tres_pc])
    spamwriter.writerow('_________Veiculo_____')                    
    spamwriter.writerow(['Moto', moto])
    spamwriter.writerow(['Carro', carro])
    spamwriter.writerow(['Ônibus', onibus])
    spamwriter.writerow(['Outros', outro_loc])
    spamwriter.writerow('_________Salarios na casa _____')                    
    spamwriter.writerow(['Até Um salário mínimo', um_salario])
    spamwriter.writerow(['Até Dois salários', dois_sm])
    spamwriter.writerow(['Até Tres salários', tres_sm])
    spamwriter.writerow(['Até Quatro salários', quatro_sm])
    spamwriter.writerow(['Até cinco salários', cinco_sm])
    spamwriter.writerow(['Acima de cinco salários', acima_cinco])
    spamwriter.writerow('_________periodo que estuda_____')                    
    spamwriter.writerow(['Estudam de manhã', manha])
    spamwriter.writerow(['Estudam a noite', noite])
    spamwriter.writerow('_________Tipo de escola_____')                    
    spamwriter.writerow(['Estudaram em escola pública', int_public])
    spamwriter.writerow(['Estudaram maior parte em escola particular', int_particular])
    spamwriter.writerow(['Estudaram maior parte em escola pública', maior_public])
    spamwriter.writerow(['Estudaram em período integral em escola particular', int_partic])
    spamwriter.writerow('_________COnhece informatica_____')                   
    spamwriter.writerow(['Tem conhecimento', conhece_info])
    spamwriter.writerow(['Não tem conhecimento', not_info])
    spamwriter.writerow(['Inválido', inv_info])
    spamwriter.writerow('_________quais conhecimentos_____')                    
    spamwriter.writerow(['Word', word])
    spamwriter.writerow(['Excel', excel])
    spamwriter.writerow(['Windows', windows])
    spamwriter.writerow(['Excel e Windows', outros_app1])
    spamwriter.writerow(['Excel, Windows, Word e outros', outros_app2])
    spamwriter.writerow(['Excel Windows e Word', outros_app3])
    spamwriter.writerow(['Windows, Word e outros', outros_app4])
    spamwriter.writerow(['Excel, Word e outros', outros_app5])
    spamwriter.writerow(['Outros', outros_app6])
    spamwriter.writerow(['Inválido', inv_app])
    spamwriter.writerow('_________idioma_____')                    
    spamwriter.writerow(['Inglês', ingles])
    spamwriter.writerow(['Inglês e alemão', ing_ale])
    spamwriter.writerow(['Inglês e italiano', ing_it])
    spamwriter.writerow(['Inglês e espanhol', ing_esp])
    spamwriter.writerow(['Espanhol', esp])
    spamwriter.writerow(['Nenhum', no_idioma])
    spamwriter.writerow('_________estudou anteriormente_____')                    
    spamwriter.writerow(['Sim', estud_escola])
    spamwriter.writerow(['Não', not_estud])
    spamwriter.writerow(['Inválido', babaca])
    spamwriter.writerow('_________qual curso_____')                   
    spamwriter.writerow(['ADS', ads])
    spamwriter.writerow(['GPI', gpi])
    spamwriter.writerow(['ADS Inválido', ads_inv])
    spamwriter.writerow('_________qual ano_____')                    
    spamwriter.writerow(['Ano 2015', ano_fatec])
    spamwriter.writerow(['Ano 2011', ano_dois])
    spamwriter.writerow('_________Motivo vestibular_____')                    
    spamwriter.writerow(['Por indicação', indicacao])
    spamwriter.writerow(['Por qualidade e/ou gratuidade', qualidade])
    spamwriter.writerow(['Para ter graduação', graduacao])
    spamwriter.writerow(['Outros', outros_mot])


print('-' *10,'*****Tabela Idade*****', '-' *10 )
print ("Há {}, ate vinte".format(vinte))
print ("Há {}, mais de vinte e ate trinta".format(atetrinta))
print ("Há {}, mais de trinta e ate quarenta".format(atequart))
print ("Há {}, mais quarenta".format(maisquart))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Genero*****', '-' *10 )
print ("Há {}, homens".format(s_masc))
print ("Há {}, mulheres".format(s_fem))
print('_'*80)
print('_'*80)
print('-' *10,'***** Tabela Cor*****', '-' *10 )
print ("Há {}, Brancos".format(c_branco))
print ("Há {}, Negros".format(c_preto))
print ("Há {}, Pardos".format(c_pardo))
print ("Há {}, Amarelos".format(c_amarelo))
print ("Há {}, outros".format(c_outro))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Religião*****', '-' *10 )
print ("Há {}, Catolicos".format(r_catolico))
print ("Há {}, Ateus".format(r_ateu))
print ("Há {}, Evangelicos".format(r_evangelica))
print ("Há {}, Agnosticos".format(r_agnostico))
print ("Há {}, Espiritas".format(r_espirita))
print ("Há {}, Outros".format(r_outros))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Estado Civil*****', '-' *10 )
print ("Há {}, Solteiros".format(ec_solteiro))
print ("Há {}, Casados".format(ec_casado))
print ("Há {}, Outros".format(ec_outros))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Deficiencia*****', '-' *10 )
print ("Há {}, Sem dificiencia".format(t_deficiencia))
print ("Há {}, Com deficiencia auditiva".format(deficiencia_aud))
print ("Há {}, com deficiencia visual".format(deficiencia_visu))
print ("Há {}, com deficiencia de fala".format(deficiencia_fala))
print ("Há {}, com outros".format(deficiencia_outros))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Filhos*****', '-' *10 )
print ("Há {}, sem filhos".format(t_filhos))
print ("Há {}, Um filho".format(um_filho))
print ("Há {}, dois filhos".format(dois_filhos))
print ("Há {}, tres ou mais".format(tresoumais))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela em que area trabalha*****', '-' *10 )
print ("Há {}, Nunca trabalhou".format(n_trabalhei))
print ("Há {}, Desempregado".format(t_desempregado))
print ("Há {}, Trabalha fora da area".format(t_fora_a_escolha))
print ("Há {}, Trabalha dentro da area".format(t_area_escolha))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Periodo Trabalho*****', '-' *10 )
print ("Há {}, Trabalham em periodo integral ".format(p_t_m_t))
print ("Há {}, Trabalham meio perioso (manhã OU tarde)".format(p_t_mout))
print ("Há {}, Trabalham em regime de turnos".format(p_t_r_t))
print ("Há {}, Trabalham a noite".format(p_t_n))
print ("Há {}, Inválido".format(cuzao))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Estados*****', '-' *10 )
print ("Há {}, que moram em SP ".format(e_sp))
print ("Há {}, que moram em MG ".format(e_mg))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Cidade*****', '-' *10 )
print ("Há {}, moram em franca ".format(m_fran))
print ("Há {}, moram em ipuã ".format(m_ipua))
print ("Há {}, moram em restinga ".format(m_rest))
print ("Há {}, moram em outro municipio ".format(m_outro))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Imovel*****', '-' *10 )
print ("Há {}, imovel proprio ".format(imo_pro))
print ("Há {}, imovel alugado ".format(imo_alug))
print ("Há {}, imovel financiado ".format(imo_fin))
print ("Há {}, imovel cedido".format(imo_ced))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Tempo moradinha*****', '-' *10 )
print('{} ate dez anos'.format(atedez))
print('{} ate vinte anos'.format(atevinte))
print('{} mais de vinte anos'.format(maisvinte))

print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Com quem mora*****', '-' *10 )
print ("Há {}, Familia(pais/parentes ".format(mora_com_familia))
print ("Há {}, Conjulgue ".format(mora_com_comp))
print ("Há {}, Familia do compranheiro ".format(mora_com_famcomp))
print ("Há {}, Outros".format(mora_outros))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Quantas pessoas moram na residencia*****', '-' *10 )
print ("Há {}, de uma a tres pessoas ".format(tot_pessum))
print ("Há {}, de quatro a seis pessoas ".format(tot_pessquat))
print ("Há {}, mais de seis ".format(tot_pessixmais))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela  Pessoas que trabalham*****', '-' *10 )
print ("Há {}, Uma pessoa trabalha ".format(pes_remune))
print ("Há {}, Duas pessoas trabalham ".format(duas_remune))
print ("Há {}, Três pessoas trabalham ".format(tres_remune))
print ("Há {}, Quatro pessoas trabalham".format(quat_remune))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Computadores*****', '-' *10 )
print ("Há {}, Sem computador ".format(no_pc))
print ("Há {}, um compuador ".format(um_pc))
print ("Há {}, dois computadores ".format(dois_pc))
print ("Há {}, tres ou mais computadores ".format(tres_pc))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Locomoção*****', '-' *10 )
print ("Há {}, Moto".format(moto))
print ("Há {}, Carro ".format(carro))
print ("Há {}, Onibus ".format(onibus))
print ("Há {}, Outros ".format(outro_loc))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Salarios Minimos*****', '-' *10 )
print ("Há {}, ate Um salario minimo".format(um_salario))
print ("Há {}, ate Dois salarios ".format(dois_sm))
print ("Há {}, ate Três salarios ".format(tres_sm))
print ("Há {}, ate Quatro salários ".format(quatro_sm))
print ("Há {}, ate Cinco salários ".format(cinco_sm))
print ("Há {}, acima de Cinco salários ".format(acima_cinco))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Periodo que estuda*****', '-' *10 )
print ("Há {}, estudam de manhã".format(manha))
print ("Há {}, estudam a noite ".format(noite))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela vida escolar*****', '-' *10 )
print ("Há {}, que estudou  escola publica ".format(int_public))
print ("Há {}, que estudo maior parte em escola particular".format(int_particular))
print ("Há {}, que estudou maior parte em escola publica".format(maior_public))
print ("Há {}, que estudou em periodo integral em escola particular ".format(int_partic))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Conhecimento Informatica*****', '-' *10 )
print ("Há {}, tem conhecimento".format(conhece_info))
print ("Há {}, Não tem ".format(not_info))
print ("Há {}, Invalido ".format(inv_info))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Quais Conhecimentos*****', '-' *10 )
print ("Há {}, word".format(word))
print ("Há {}, excel ".format(excel))
print ("Há {}, windows ".format(windows))
print ("Há {}, com conhecimento em Excel, Windows".format(outros_app1))
print ("Há {}, com conhecimento em Excel, Windows, Word, Outros".format(outros_app2))
print ("Há {}, com conhecimento em Excel, Windows, Word".format(outros_app3))
print ("Há {}, com conhecimento em Windows, Word, Outros".format(outros_app4))
print ("Há {}, com conhecimento em Excel, Word, Outros".format(outros_app5))
print ("Há {}, com conhecimento em Outros".format(outros_app6))
print ("Há {}, invalido ".format(inv_app))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Idioma*****', '-' *10 )
print ("Há {}, Ingles".format(ingles))
print ("Há {}, Ingles e alemão ".format(ing_ale))
print ("Há {}, Ingles e italino ".format(ing_it))
print ("Há {}, Ingles e espanhol ".format(ing_esp))
print ("Há {}, Espanhol ".format(esp))
print ("Há {}, Nenhum ".format(no_idioma))
print('_'*80)
print('_'*80)
print('-' *10,'*****Tabela Já foi aluno da fatec*****', '-' *10 )
print ("Há {}, sim".format(estud_escola))
print ("Há {}, Não ".format(not_estud))
print("Há {}, inválido".format(babaca))
print('_'*80)
print('_'*80)
print('-' *10,'*****Qual Curso*****', '-' *10 )
print ("Há {}, ads".format(ads))
print ("Há {}, gpi ".format(gpi))
print("Há {}, Ads inválido".format(ads_inv))
print('_'*80)
print('_'*80)
print('-' *10,'*****Qual Curso*****', '-' *10 )
print ("Há {}, Ano 2015".format(ano_fatec))
print ("Há {}, Ano 2011".format(ano_dois))
print('_'*80)
print('_'*80)
print('-' *10,'*****Motivação*****', '-' *10 )
print ("Há {}, por indicação".format(indicacao))
print ("Há {}, por qualidade e/ou gratuidade".format(qualidade))
print ("Há {}, para ter graduação".format(graduacao))
print ("Há {}, de outros motivos".format(outros_mot))

print('made by: Luana do Nascimento Ferreira')
