from bs4 import BeautifulSoup
from prettytable import PrettyTable
def parser_gvGameHtml_Props(html):
    Props = []

    try:
        soup = BeautifulSoup(html, 'lxml')

        horizons = soup.find_all(class_='form-horizontal')

        for horizon in horizons:
            nameProps = horizon.span.text
            listOutCome2 = horizon.find_all(id='listOutCome2')
            prop = []
            for out in listOutCome2:
                prop.append(
                    {
                        'name': out.div.text,
                        'value': out.find_all('div')[1].div.text
                    }
                )
            Props.append(
                {
                    'title': nameProps,
                    'Prop': prop

                }
            )
    except Exception as err:
        raise
        print(f'Ошибка парсинга gvGameHtml: {err}')
    return Props

def parser_gvGameHtml_Html(html, sport):
    Score = {}
    comand1 = ''
    comand2 = ''
    comand1_score = 0
    comand2_score = 0
    Score1 = []
    Score2 = []
    timeOut = []

    if sport in ['Soccer']:
        soup = BeautifulSoup(html,'lxml')
        comand1 = soup.find(id ='gameHeading').find_all(class_ = 'team')[0].text
        comand2 = soup.find(id ='gameHeading').find_all(class_ = 'team')[1].text
        comand1_score = soup.find(id ='gameHeading').find_all(class_ = 'score')[0].text
        comand2_score = soup.find(id ='gameHeading').find_all(class_ = 'score')[1].text

        timeOuts = soup.find_all('th', class_ ='per')
        for out in timeOuts:
            timeOut.append(out.text)
        size = len(soup.find_all('th', class_ ='per'))

        for temp in soup.find_all('td', class_ ='per')[:size]:
            Score1.append(temp.text.strip())

        for temp in soup.find_all('td', class_ ='per')[size:]:
            Score2.append(temp.text.strip())


        a= ['']
        a.extend(timeOut)
        table = PrettyTable(a)
        a = [comand1]
        a.extend(Score1)
        table.add_row(a)
        a = [comand2]
        a.extend(Score2)
        table.add_row(a)

        Score = {
            'comman1': comand1,
            'comman2': comand2,
            'comand1_score' : comand1_score,
            'comand2_score' : comand2_score,
            'timeOut' : timeOut,
            'score1' : Score1,
            'score2' : Score2,
            'table': table
        }

    return Score



    pass


html = """

<!-- Begin ~/Skin/{0}/Content/gvGame.ascx -->

<div id="pnGameHeadScoreBoard">
</div>
    <div id="gvGameFixed" class="Soccer progSoccer" leagueid="189" brmatchid="34152091">
	
    <div class="gameHead">
        <div class="sportGlyph" />
        
            <div class="sport">Soccer</div>
            <div class="league">England - Premier League</div>                    
              
        
        <script>
            $("#gvGame,#gvGameScrolling").attr("sport", 'Soccer');
        </script>        
    </div>
    
    

<div id="gameHeading" class="col-md-10 col-xs-10 col-sm-10 col-xs-offset-1 col-sm-offset-1 col-md-offset-1">
    <table class="table FullScore Soccer">
        <tbody>
            <tr>
                <td class="team away">FULHAM</td>
                
                        <td class="score"><div class="scores taway">0</div></td>
                
                        
                <td class="versus "></td>
                        
                
                        <td class="score"><div class="scores thome">0</div></td>  
                
                <td class="team home">TOTTENHAM</td>
            </tr>
        </tbody>
    </table>
</div>
<!-- Begin ~/Skin/{0}/Content/GameProgressSoccer.ascx -->
<div class="scoreProgress col-xs-offset-3 col-sm-offset-3 col-md-offset-3 col-md-6 col-xs-6 col-sm-6">
    <table class="table soccerFullScore 1st">
        <tr>
            <th class="team"></th>
            
                    
                    <th class="per">1st Half</th>
                
                    
                    <th class="per">2nd Half</th>
                
            
        </tr>
        <tr>
            <td class="team">FULHAM</td>
            
                    
                     <td class="per last home">
                        <div>
                            0
                        </div>                     
                    </td>
                
                    
                     <td class="per ">
                        <div>
                            
                        </div>                     
                    </td>
                
            
            <td class="status" rowspan="2">1st<br />5:34m</td>
        </tr>
        <tr>
            <td class="team">TOTTENHAM</td>
            
                    
                     <td class="per last away">
                        <div>
                            0
                        </div>                     
                    </td>
                
                    
                     <td class="per ">
                        <div>
                            
                        </div>                     
                    </td>
                
            
        </tr>
    </table>
</div>
<!-- End ~/Skin/{0}/Content/GameProgressSoccer.ascx -->

    

</div>
<div id="div-livestreaming" style="display: none">
</div>
<div id="div-matchtracker" style="display: none">
</div>
<!-- End ~/Skin/{0}/Content/gvGame.ascx -->

"""
#print(parser_gvGameHtml_Html(html,'Soccer'))
