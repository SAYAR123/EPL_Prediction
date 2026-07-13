import streamlit as st
import os
import base64
from ui import hero, match_info

# Define the absolute path safely as a raw string to handle Windows backslashes
logo_folder = r"C:\Projects\football_final\frontend\logos" 

# Your clean helper function to convert the image to a Data URL
def get_base64_image(image_path):
    if os.path.exists(image_path):
        try:
            with open(image_path, "rb") as img_file:
                encoded_string = base64.b64encode(img_file.read()).decode()
            return f"data:image/png;base64,{encoded_string}"
        except Exception:
            pass
    # Return None if file is missing or unreadable so Streamlit handles fallback cleanly
    return None

def show_about_page():
    
    hero(
        'About the English Premier League (EPL)',
        'Founded in 1992 following the breakaway from the Football League First Division, the English Premier League (EPL) has grown into the most-watched sports league in the world. Broadcast to over 800 million homes across 188 countries, it is renowned for its unparalleled unpredictability, blistering pace, and global star power.'
    )

    # Quick Stats Banner
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    col_stat1.metric("Format", "20 Clubs")
    col_stat2.metric("System", "Promotion/ Relegation")
    col_stat3.metric("Matches/ Season", "380 Total")
    
    with st.expander("League Format & Global Icons", expanded=True):
        st.markdown("""
        * **The Format:** Running from August to May, each team plays the others twice (home and away) for a total of 38 matches. The top 4 teams qualify directly for the prestigious **UEFA Champions League**, while the bottom 3 are brutally relegated to the EFL Championship.
        * **Historic Figures:** The league has been graced by icons who shaped modern football—from the goalscoring supremacy of **Alan Shearer** (260 goals) and the wizardry of **Thierry Henry**, to midfield maestros like **Steven Gerrard**, **Frank Lampard**, and modern titans like **Kevin De Bruyne** and **Mohamed Salah**.
        """)
        
    st.write("---")
    
    # -------------------------------------------------------------
    # SECTION 2: CLUB DEEP DIVE DIRECTORY
    # -------------------------------------------------------------
    st.subheader("Club Directory (Historical Data: 2000–Present)")
    st.write("Select any of the 46 teams present in our dataset to view their legacy, historical significance, and modern status.")
    
    # Comprehensive dictionary mapping out the specific traits of all 46 clubs
    club_data = {
        "Arsenal": {
            "founded": 1886, 
            "players": "Thierry Henry, Dennis Bergkamp, Bukayo Saka", 
            "status": "Active (Title Contender)", 
            "desc": "Founded by munitions workers in Woolwich before moving to North London, Arsenal boasts one of the richest legacies in English football. They are historically celebrated for their 2003/04 'Invincibles' season under Arsène Wenger, going an entire league campaign undefeated. Known traditionally for fluid, possession-heavy attacking football, the club has transformed into a relentless tactical powerhouse under Mikel Arteta, consistently challenging at the absolute summit of the modern Premier League."
        },
        "Aston Villa": {
            "founded": 1874, 
            "players": "Jack Grealish, Ollie Watkins, Emiliano Martínez", 
            "status": "Active (European Contender)", 
            "desc": "As a proud founding member of both the Football League and the Premier League, Aston Villa is a historical giant located in Birmingham. The club reached the pinnacle of European football by winning the European Cup in 1982. Following a painful relegation in 2016, they successfully rebuilt their identity. Under the astute tactical leadership of Unai Emery, Villa has transformed into a high-pressing, elite modern force, regularly qualifying for European competitions and disrupting the traditional top-six hierarchy."
        },
        "Blackburn": {
            "founded": 1875, 
            "players": "Alan Shearer, Chris Sutton, Blackburn Legends", 
            "status": "EFL Championship", 
            "desc": "Hailing from Lancashire, Blackburn Rovers holds a legendary distinction as one of the few clubs to win the modern Premier League title, lifting the trophy in the iconic 1994/95 season powered by the famous 'SAS' striking partnership of Alan Shearer and Chris Sutton. Following financial instabilities, the club was relegated from the top flight in 2012. They are currently an ambitious fixture in the EFL Championship, consistently fighting to rebuild their squad and reclaim their historic place in the Premier League."
        },
        "Blackpool": {
            "founded": 1887, 
            "players": "Sir Stanley Matthews, Charlie Adam, Brett Ormerod", 
            "status": "EFL League One", 
            "desc": "Famed for their distinctive tangerine kits and the legacy of the legendary Sir Stanley Matthews, Blackpool is a historic seaside club. They captured the hearts of global fans during a chaotic, highly entertaining solo cameo season in the Premier League back in 2010/11 under Ian Holloway, defined by a fearless 'attack-at-all-costs' philosophy. Following severe financial ownership crises that dropped them down the leagues, they are currently competing in EFL League One, working to stabilize their football operations."
        },
        "Bolton": {
            "founded": 1874, 
            "players": "Jay-Jay Okocha, Nicolas Anelka, Kevin Davies", 
            "status": "EFL League One", 
            "desc": "Bolton Wanderers were a widely feared, iconic fixture of the Premier League throughout the mid-2000s under Sam Allardyce. Renowned for combining highly physical, direct aerial tactics with flair players like Jay-Jay Okocha, they regularly qualified for Europe and upset elite teams. Massive financial debts eventually forced them out of the top flight in 2012, even pushing them to the brink of extinction. Today, they are a stabilized club in EFL League One, steadily rebuilding toward the upper tiers."
        },
        "Bournemouth": {
            "founded": 1899, 
            "players": "Callum Wilson, Dominic Solanke, Antoine Semenyo", 
            "status": "Active (Mid-Table)", 
            "desc": "Bournemouth represents one of the most remarkable fairytales in modern football history. Pushed to the absolute brink of financial bankruptcy and liquidation in the bottom tier of English football in 2008, a meteoric rise engineered by manager Eddie Howe saw them reach the Premier League by 2015. Known for their fast, progressive transition play and incredibly smart recruitment, the 'Cherries' have successfully solidified their status as a resilient, highly competitive mid-table Premier League main stay."
        },
        "Bradford": {
            "founded": 1903, 
            "players": "Dean Windass, Benito Carbone, Stuart McCall", 
            "status": "EFL League Two", 
            "desc": "Bradford City enjoyed a memorable two-season spell in the Premier League at the turn of the millennium. Their stay was highlighted by an iconic final-day 'Great Escape' in the 1999/2000 season, where a legendary David Wetherall header defeated Liverpool to secure their safety. Subsequent financial collapses triggered a long slide down the football pyramid. The club currently competes in EFL League Two, backed by a famously passionate, large fanbase eager for a return to past glory."
        },
        "Brentford": {
            "founded": 1889, 
            "players": "Ivan Toney, Bryan Mbeumo, Yoane Wissa", 
            "status": "Active (Mid-Table)", 
            "desc": "Hailing from West London, Brentford is universally praised as the gold standard for data-driven, analytical 'moneyball' recruitment models in football. After earning a historic promotion to the Premier League in 2021, Thomas Frank’s side instantly adapted to the top flight. Utilizing lethal set-piece routines, structural discipline, and quick counter-attacking combinations, the 'Bees' have become a highly competent mid-table side with a reputation for routinely upsetting the league's elite."
        },
        "Brighton": {
            "founded": 1901, 
            "players": "Lewis Dunk, Kaoru Mitoma, Joao Pedro", 
            "status": "Active (European Contender)", 
            "desc": "Brighton & Hove Albion's modern rise is a masterpiece of corporate and sporting strategy. Nearly losing their professional status in the late 90s, the Seagulls moved into the Amex Stadium and earned Premier League promotion in 2017. They are globally revered for an unparalleled global scouting network that unearths hidden gems. Playing highly progressive, possession-dominant football, Brighton has established itself as a regular contender for European places and a model footballing institution."
        },
        "Burnley": {
            "founded": 1882, 
            "players": "Kieran Trippier, Nick Pope, James Tarkowski", 
            "status": "EFL Championship", 
            "desc": "One of the oldest professional clubs in the world, Burnley is deeply woven into the fabric of English football. Under Sean Dyche, the club became famous for an incredibly rigid, defensive, and physically demanding 4-4-2 system that punching way above its weight, even qualifying for Europe in 2018. Following a transition period between styles and ownerships, they have spent recent seasons navigating the gap between divisions and are currently fighting at the top end of the EFL Championship."
        },
        "Birmingham": {
            "founded": 1875, 
            "players": "Christophe Dugarry, Jude Bellingham, Mikael Forssell", 
            "status": "EFL League One", 
            "desc": "Birmingham City is a passionate, gritty Midlands club that enjoyed several prolonged, competitive spells in the Premier League during the 2000s. Their finest modern hour came in 2011, when they defeated Arsenal in dramatic fashion to lift the League Cup, only to be relegated from the top flight just months later. Famously the academy birthplace of superstar Jude Bellingham, the club has recently undergone major high-profile ownership changes and is aggressively rebuilding from EFL League One."
        },
        "Cardiff": {
            "founded": 1899, 
            "players": "Peter Whittingham, Aron Gunnarsson, Sol Bamba", 
            "status": "EFL Championship", 
            "desc": "As the only non-English club to have ever won the FA Cup (back in 1927), Cardiff City carries the pride of Welsh football history. The Bluebirds achieved hard-fought promotion campaigns to the modern Premier League in both 2013 and 2018, providing the league with fiery atmospheric derbies. While both stints ended in immediate relegation, the club remains an intensely competitive and highly physical fixture in the EFL Championship, looking to steady their structure for another promotion push."
        },
        "Charlton": {
            "founded": 1905, 
            "players": "Darren Bent, Scott Parker, Clive Mendonca", 
            "status": "EFL League One", 
            "desc": "Based in South London, Charlton Athletic was the epitome of Premier League stability throughout the late 1990s and early 2000s. Under the steady guidance of Alan Curbishley, they established themselves as a highly respected, top-half top-flight side. Following Curbishley’s departure and subsequent relegation in 2007, ownership disputes and financial instability saw them slide down the pyramid. They are currently working on building structural stability inside EFL League One."
        },
        "Chelsea": {
            "founded": 1905, 
            "players": "Frank Lampard, Didier Drogba, Cole Palmer", 
            "status": "Active (Top 6 Contender)", 
            "desc": "Chelsea's trajectory was forever altered in 2003, sparking a trophy-laden era that transformed them into a global superpower. Renowned historically for defensive steel under Jose Mourinho and high-profile signings, the Blues have captured multiple Premier League, FA Cup, and UEFA Champions League trophies. Now under new ownership, the club has invested heavily in assembling an elite pool of young global talent, playing an aggressive possession style while firmly aiming to reclaim permanent top-four status."
        },
        "Coventry": {
            "founded": 1883, 
            "players": "Dion Dublin, Robbie Keane, Viktor Gyökeres", 
            "status": "EFL Championship", 
            "desc": "Coventry City was a foundational pillar of the modern Premier League breakaway in 1992, completing an astonishing 34 consecutive years in the top flight of English football. Following their heartbreaking relegation in 2001, the club suffered decades of severe financial crises, stadium displacement, and a drop to the fourth tier. Staged a heroic structural comeback in recent years, they have re-established themselves as an exciting, attacking contender in the EFL Championship."
        },
        "Crystal Palace": {
            "founded": 1905, 
            "players": "Wilfried Zaha, Eberechi Eze, Marc Guéhi", 
            "status": "Active (Mid-Table)", 
            "desc": "Hailing from South London, Crystal Palace is legendary for its production of electric, dynamic wingers and boasting one of the most vocal, European-style atmospheres in the UK at Selhurst Park. After securing promotion in 2013, the Eagles defied early tags to become a highly consistent, bulletproof Premier League mainstay. Known for their structural resilience, the club has evolved to embrace an incredibly exciting, youthful attacking philosophy that safely anchors them in mid-table."
        },
        "Derby": {
            "founded": 1884, 
            "players": "Paulo Wanchope, Igor Štimac, Wayne Rooney", 
            "status": "EFL Championship", 
            "desc": "Derby County is a historic powerhouse of English football, having won two First Division titles in the 1970s under Brian Clough. In the Premier League era, they are famous for an exciting late-90s team, but also hold the infamous, painful record for the lowest points total in Premier League history (11 points in 2007/08). After surviving a devastating recent period of administration and points deductions, the Rams have proudly bounced back into the EFL Championship."
        },
        "Everton": {
            "founded": 1878, 
            "players": "Tim Cahill, Leighton Baines, Romelu Lukaku", 
            "status": "Active (Historic Mainstay)", 
            "desc": "Everton is a true titan of English football history, holding the record for the most historic seasons spent in the top flight. A founding member of the league, the Toffees have maintained an unbroken stay in the Premier League since 1992. Despite facing severe financial hurdles, regulatory point deductions, and intense relegation scares in recent seasons, their grit, combined with a passionate fanbase and a transition into a state-of-the-art new stadium, keeps them anchored in the top flight."
        },
        "Fulham": {
            "founded": 1879, 
            "players": "Clint Dempsey, Aleksandar Mitrović, Andreas Pereira", 
            "status": "Active (Mid-Table)", 
            "desc": "As London's oldest professional football club, Fulham is famous for its historic, picturesque home ground, Craven Cottage. After spending the 2000s as a competitive top-flight outfit—even reaching a European final in 2010—they endured a prolonged 'yo-yo' phase between divisions. Under Marco Silva, the club has permanently broken that cycle, playing an elegant, tactically balanced brand of football that has firmly re-established them as a competitive top-flight asset."
        },
        "Huddersfield": {
            "founded": 1908, 
            "players": "Aaron Mooy, Christopher Schindler, prospective stars", 
            "status": "EFL League One", 
            "desc": "Huddersfield Town holds a legendary status in English football history as the very first club to win three consecutive top-flight league titles in the 1920s under Herbert Chapman. In 2017, they captured global attention by orchestrating a stunning fairy-tale promotion to the Premier League under David Wagner. They managed a historic survival season before being relegated in 2019. The Terriers are currently focused on rebuilding their squad and structure within EFL League One."
        },
        "Hull": {
            "founded": 1904, 
            "players": "Geovanni, Jarrod Bowen, Andrew Robertson", 
            "status": "EFL Championship", 
            "desc": "Hull City spent the first century of their history outside the top flight before securing a historic first-ever promotion to the Premier League in 2008. The Tigers enjoyed an exciting, chaotic presence across multiple stints in the 2010s, highlighted by an unforgettable run to the FA Cup Final in 2014. After dropping down the leagues, they have stabilized under ambitious new international ownership, competing actively in the EFL Championship with an eye on top-flight return."
        },
        "Ipswich": {
            "founded": 1878, 
            "players": "Marcus Stewart, Matt Holland, Leif Davis", 
            "status": "Active (Promoted)", 
            "desc": "Boasting a rich historical pedigree that includes an English League Title and a UEFA Cup under legendary managers Sir Alf Ramsey and Sir Bobby Robson, Ipswich Town is deeply respected. After a painful 22-year absence from the top flight, the club pulled off an astonishing, historic back-to-back promotion campaign under the tactical brilliance of Kieran McKenna. They are currently fighting fiercely to adapt their modern, fluid passing style to secure long-term Premier League survival."
        },
        "Leeds": {
            "founded": 1919, 
            "players": "Mark Viduka, Kalvin Phillips, Raphinha", 
            "status": "EFL Championship", 
            "desc": "Leeds United is a massive institutional club with a famously passionate, intensely loyal global fanbase. After reaching the semi-finals of the UEFA Champions League in 2001, a catastrophic financial collapse forced a devastating 16-year exile from the top flight. They were famously revived by the revolutionary high-intensity tactics of Marcelo Bielsa in 2020. Relegated again in 2023, the Whites are currently operating as a high-budget powerhouse in the EFL Championship, determined to go back up."
        },
        "Leicester": {
            "founded": 1884, 
            "players": "Jamie Vardy, Riyad Mahrez, N'Golo Kanté", 
            "status": "Active (Mid-Table)", 
            "desc": "Leicester City authored the single most spectacular, mind-boggling miracle in the history of global sports by defying 5000-1 odds to win the Premier League title in the 2015/16 season. The club followed it up with historic European runs and an FA Cup triumph in 2021. Shockingly relegated in 2023, they showed immense resilience by bouncing back immediately as Championship winners. They are now focused on preserving their top-flight status, led by veteran talisman Jamie Vardy."
        },
        "Liverpool": {
            "founded": 1892, 
            "players": "Steven Gerrard, Mohamed Salah, Virgil van Dijk", 
            "status": "Active (Title Contender)", 
            "desc": "Liverpool is a true colossus of global sport, possessing a trophy cabinet filled with domestic league titles and multiple historic European Cups. The club is world-famous for the electric atmosphere of Anfield and their iconic 'You'll Never Walk Alone' anthem. After breaking their 30-year title drought under Jürgen Klopp with an intense, heavy-metal pressing style, the club has smoothly transitioned into a new tactical era, continuing to act as a permanent, elite title contender."
        },
        "Luton": {
            "founded": 1885, 
            "players": "Ross Barkley, Tom Lockyer, Carlton Morris", 
            "status": "EFL Championship", 
            "desc": "Luton Town’s journey is arguably the most romantic climb in modern football history. Dropping completely out of the professional football league into non-league amateur status in 2009 due to financial penalties, they engineered a historic rise through five divisions to reach the Premier League in 2023. Their tight, atmospheric home ground, Kenilworth Road, became a symbol of romantic football. Following a heroic top-flight campaign, they are currently utilizing that core structure in the EFL Championship."
        },
        "Man City": {
            "founded": 1880, 
            "players": "Sergio Agüero, Kevin De Bruyne, Erling Haaland", 
            "status": "Active (Elite Title Holders)", 
            "desc": "Manchester City has completely rewritten the record books of English football over the last two decades. Evolving into a dominant global empire, the club reached historical perfection under Pep Guardiola, becoming the first English side to secure a 100-point season and winning a historic European Treble. Playing a mesmerizing, structurally perfect positional possession game, City enters every single season as the benchmark elite force to beat in modern football."
        },
        "Man United": {
            "founded": 1878, 
            "players": "Sir Bobby Charlton, Cristiano Ronaldo, Wayne Rooney", 
            "status": "Active (Top 6 Contender)", 
            "desc": "Manchester United is arguably the most commercially massive and historically dominant institution in Premier League history. Under the legendary 26-year reign of Sir Alex Ferguson, the club established a global empire built on attacking wing play, iconic youth development, and dramatic late comebacks. Navigating a complex, highly scrutinized transition period in the post-Ferguson era, the Red Devils remain a top-six heavyweight consistently aiming to restore their domestic dominance."
        },
        "Middlesbrough": {
            "founded": 1876, 
            "players": "Juninho, Jimmy Floyd Hasselbaink, Gareth Southgate", 
            "status": "EFL Championship", 
            "desc": "Based in the Northeast, Middlesbrough was a vibrant, star-studded destination throughout the late 1990s and 2000s, famously attracting elite global stars like Juninho and reaching the UEFA Cup Final in 2006. Relegated in 2009, 'Boro' has spent the majority of the last decade trying to replicate those golden top-flight years. Under progressive modern coaching, they operate as a dangerous, tactically flexible promotion contender in the EFL Championship pyramid."
        },
        "Newcastle": {
            "founded": 1892, 
            "players": "Alan Shearer, Alexander Isak, Bruno Guimarães", 
            "status": "Active (European Contender)", 
            "desc": "Newcastle United is backed by one of the most intensely passionate, dedicated one-club-city fanbases in global football. Famed for the iconic black-and-white stripes and the goalscoring record of Alan Shearer, the club spent years trapped in stagnation before a transformative takeover injected massive financial stability. Now playing a high-intensity, aggressive pressing game under Eddie Howe, the Magpies have successfully broken back into European contention."
        },
        "Norwich": {
            "founded": 1902, 
            "players": "Teemu Pukki, Grant Holt, James Maddison", 
            "status": "EFL Championship", 
            "desc": "Norwich City is famously recognized by their vibrant yellow-and-green branding and their deep-rooted community ethos. Throughout the 2010s, the Canaries became the definitive 'yo-yo' club of English football, dominating the Championship to win promotion, only to suffer immediate relegation due to a strict adherence to open, attacking football on a sustainable budget. They are currently maintaining their technical, progressive identity as an EFL Championship regular."
        },
        "Nott'm Forest": {
            "founded": 1865, 
            "players": "Keylor Navas, Morgan Gibbs-White, Taiwo Awoniyi", 
            "status": "Active (Mid-Table)", 
            "desc": "Nottingham Forest possesses a legendary historical pedigree, having won back-to-back European Cups in 1979 and 1980 under the eccentric genius of Brian Clough. Following a grueling, painful 23-year absence from the top flight, the club made a dramatic return to the Premier League in 2022. Backed by an incredibly active recruitment strategy and a booming, hostile home crowd at the City Ground, Forest has evolved into an incredibly dangerous, fast counter-attacking mid-table side."
        },
        "Portsmouth": {
            "founded": 1898, 
            "players": "Jermain Defoe, Nwankwo Kanu, Peter Crouch", 
            "status": "EFL Championship", 
            "desc": "Portsmouth achieved explosive, highly memorable success in the mid-to-late 2000s, famously capturing the FA Cup in 2008 at Wembley stadium while maintaining a star-studded Premier League roster. However, severe financial mismanagement and astronomical debts triggered a catastrophic collapse, leading to consecutive relegations all the way down to the fourth tier. Following a long, grueling journey of financial stabilization, 'Pompey' has proudly fought their way back into the EFL Championship."
        },
        "QPR": {
            "founded": 1882, 
            "players": "Adel Taarabt, Charlie Austin, Les Ferdinand", 
            "status": "EFL Championship", 
            "desc": "Queens Park Rangers brought immense high-profile drama to West London during their modern Premier League spells in the early 2010s. Characterized by chaotic, big-budget transfer windows, veteran star signings, and frantic relegation escapes, their era was epitomized by the unpredictable individual brilliance of Adel Taarabt. After adjusting to a much more practical and financially sustainable business model, QPR is currently an established, hard-working side in the EFL Championship."
        },
        "Reading": {
            "founded": 1871, 
            "players": "Kevin Doyle, Gylfi Sigurdsson, Shane Long", 
            "status": "EFL League One", 
            "desc": "Reading etched their names into football folklore by storming to promotion in 2006 while accumulating a historic, unbroken record of 106 points in a single Championship season. They followed it up with a spectacular 8th-place finish in the Premier League. Unfortunately, severe modern financial mismanagement, ownership disputes, and subsequent strict EFL points deductions eventually dragged the Royals out of the top tiers. They are currently fighting to stabilize inside EFL League One."
        },
        "Sheffield United": {
            "founded": 1889, 
            "players": "Billy Sharp, Phil Jagielka, gustavo Hamer", 
            "status": "EFL Championship", 
            "desc": "Sheffield United is a historic, blue-collar institution representing the steel city with immense pride. Under Chris Wilder in 2019, they took the Premier League by storm, finishing in the top half using a revolutionary, highly unique 'overlapping center-backs' tactical formation. Known for their physical commitment, high work rate, and intense defensive shape, the Blades have continued to rotate between divisions in recent years and are currently working to dominate the EFL Championship."
        },
        "Southampton": {
            "founded": 1885, 
            "players": "Sadio Mané, Virgil van Dijk, James Ward-Prowse", 
            "status": "Active (Relegation Battle)", 
            "desc": "Southampton earned global acclaim in the 2010s for running one of the most elite youth academies in world football, alongside an incredible scouting system that developed modern superstars like Gareth Bale and Sadio Mané. This system allowed them to consistently finish in European spots. After a painful relegation broke that cycle, the Saints quickly bounced back to the top flight under Russell Martin, employing an extremely brave, high-risk possession philosophy as they battle for long-term survival."
        },
        "Stoke": {
            "founded": 1863, 
            "players": "Ryan Shawcross, Peter Crouch, Marko Arnautović", 
            "status": "EFL Championship", 
            "desc": "Stoke City is globally recognized as one of the oldest professional clubs in existence. Under Tony Pulis, they turned their home ground into a terrifying fortress, giving birth to the iconic football meme: 'Can they do it on a cold, rainy night in Stoke?' Built on an unyielding defensive block and Rory Delap's legendary long throws, they later transitioned to a fluid style before relegation in 2018. They are currently a rugged, rebuilding fixture in the EFL Championship."
        },
        "Sunderland": {
            "founded": 1879, 
            "players": "Jermain Defoe, Asamoah Gyan, Jordan Henderson", 
            "status": "EFL Championship", 
            "desc": "Sunderland is an absolute giant of a football club based in the Northeast, boasting the massive Stadium of Light and an intensely loyal fanbase. The club spent a decade pull off legendary, miraculous late-season relegation escapes in the Premier League before suffering consecutive drops documented globally on film. After spending years trapped in League One, the Black Cats have successfully stabilized and are playing an incredibly exciting, youth-centric style in the EFL Championship."
        },
        "Swansea": {
            "founded": 1912, 
            "players": "Michu, Gylfi Sigurdsson, Wilfried Bony", 
            "status": "EFL Championship", 
            "desc": "Swansea City brought an absolute breath of fresh air to the Premier League in 2011, earning the nickname 'Swanselona' due to their strict adherence to an elegant, Spanish-inspired tiki-taka passing game. They enjoyed a highly successful seven-year stay in the top flight, highlighted by winning the League Cup in 2013. Relegated in 2018, the Welsh side has committed to maintaining their identity as a fluid, ball-dominant passing outfit within the EFL Championship."
        },
        "Tottenham": {
            "founded": 1882, 
            "players": "Harry Kane, Gareth Bale, Son Heung-min", 
            "status": "Active (Top 6 Contender)", 
            "desc": "Tottenham Hotspur is firmly entrenched as a powerhouse member of the Premier League's 'Big Six'. Historically associated with an entertaining, high-risk philosophy of 'To Dare Is To Do,' the club modernised into a regular UEFA Champions League finalist and constructed a multi-billion pound stadium facility. Under Ange Postecoglou, Spurs have fully embraced a breathless, hyper-aggressive, ultra-high-line attacking style that makes them one of the most exciting watches in football."
        },
        "Watford": {
            "founded": 1881, 
            "players": "Troy Deeney, Odion Ighalo, Ismaila Sarr", 
            "status": "EFL Championship", 
            "desc": "Watford enjoyed a highly robust, physically dominant mid-table presence in the Premier League between 2015 and 2020, highlighted by reaching the FA Cup Final in 2019. Under the ownership of the Pozzo family, the club became widely known for its aggressive, high-frequency managerial changes. Now stabilized as an established, physically imposing outfit in the EFL Championship, the Hornets are consistently re-tooling their squad to mount a serious promotion push back to the top tier."
        },
        "West Brom": {
            "founded": 1878, 
            "players": "Chris Brunt, Peter Odemwingie, Romelu Lukaku", 
            "status": "EFL Championship", 
            "desc": "West Bromwich Albion is an iconic Midlands club that famously engineered the first modern 'Great Escape' in Premier League history, becoming the first club to survive relegation after being bottom of the table at Christmas in 2004. Known historically as a highly robust, physically imposing side that bounced frequently between the top two divisions, the Baggies are currently a well-coached, structurally disciplined defensive powerhouse fighting at the top of the EFL Championship."
        },
        "West Ham": {
            "founded": 1895, 
            "players": "Mark Noble, Dimitri Payet, Jarrod Bowen", 
            "status": "Active (Mid-Table/Europe)", 
            "desc": "Affectionately known as 'The Academy of Football' due to their history of developing iconic English talents like Bobby Moore and Declan Rice, West Ham United is a massive London institution. Playing out of the massive London Stadium, the Hammers have experienced a modern renaissance, routinely qualifying for European competitions and winning the UEFA Europa Conference League trophy in 2023. They possess a deep, high-quality squad consistently pushing to disrupt the top six."
        },
        "Wigan": {
            "founded": 1932, 
            "players": "Hugo Rodallega, Charles N'Zogbia, Leighton Baines", 
            "status": "EFL League One", 
            "desc": "Wigan Athletic pulled off impossible relegation escapes for nearly a decade in the Premier League under the guidance of Roberto Martínez. Their top-flight story reached a dramatic climax in 2013, when they pulled off a historic shock to win the FA Cup against Manchester City, only to be relegated from the Premier League in the exact same week. After suffering severe financial administration periods, the club has stabilized their operations and is currently competing in EFL League One."
        },
        "Wolves": {
            "founded": 1877, 
            "players": "Ruben Neves, Raúl Jiménez, Matheus Cunha", 
            "status": "Active (Mid-Table)", 
            "desc": "Wolverhampton Wanderers is a historic pillar of English football that underwent a massive modern renaissance following a takeover in 2016. By establishing an incredibly smart pipeline of elite Portuguese international talent, Wolves stormed into the Premier League and instantly qualified for Europe. Known for their tactical defensive discipline, compact counter-attacking shape, and explosive wing play, the club has solidified itself as a highly competent, permanent mid-table Premier League asset."
        }
    }

    # Dropdown to select a club dynamically
    teams_list = sorted(list(club_data.keys()))
    selected_club = st.selectbox("🔍 Search & Select a Club:", options=teams_list)
    
    # -------------------------------------------------------------
    # SECTION 3: DYNAMIC CLUB METRIC DISPLAY CARD
    # -------------------------------------------------------------
    if selected_club:
        club = club_data[selected_club]
        
        st.write("---")
        
        # Grid setup for Logo and Title
        col_img, col_title = st.columns([1, 4])
        
        with col_img:
            # Construct the full absolute path using os.path.join
            logo_path = os.path.join(logo_folder, f"{selected_club}.png")
            
            # Convert local image to Base64 data string using your function
            final_logo = get_base64_image(logo_path)
            
            # Render either the Base64 image or the dynamic CSS circle fallback
            if final_logo:
                st.image(final_logo, width=100)
            else:
                # Beautiful CSS fallback if the logo is missing/unreadable
                st.markdown(
                    f"<div style='background-color:#37003c; color:white; text-align:center; "
                    f"border-radius:50%; width:80px; height:80px; line-height:80px; "
                    f"font-weight:bold; font-size:32px;'>{selected_club[0]}</div>", 
                    unsafe_allow_html=True
                )

        with col_title:
            st.title(selected_club)
            st.markdown(f"**Current Competitive Status:** `{club['status']}`")

        # Info Display Layout Grid
        c1, c2 = st.columns(2)
        c1.markdown(f"**Year Founded:** `{club['founded']}`")
        c2.markdown(f"**Legendary Players:** \n*{club['players']}*")

        match_info('Brief info:')
        st.markdown(club['desc'])
    