import ollama
import re

model="deepseek-r1:7b"#or:8b
prompt="""i have two lists of song names, tell me the songs that exist in one and doesnt exist in the other


list1{
     Just the Two of Us
, Bury Me Face Down
, Alright
, Cupid - Twin Version
, 31 Freestyle
, Caterpillar (feat. Eminem & King Green)
, Careless Whisper
, Up Down (Step & Walk)
, Peaceful Sleep
, Fortress of Lies
, Weight of the World - English Version - J'Nique Nicole
, Wu Tang Forever (ft. Ghostface Killah, Raekwon, RZA, Method Man, Inspectah Deck, Cappadonna, Jackpot Scotty Wotty, U-God, Masta Killa, GZA)
, Talk talk featuring troye sivan
, Tongue - super slowed
, TiK ToK
, After LIKE
, Return of the Tres
, Von dutch
, Die Young
, Crazy In Love (feat. JAY-Z)
, I'm In Love With a Monster
, Watch The Party Die
, Like My Shit
, Murdergram Deux (feat. Eminem)
, Moral of the Story
, Softcore
, All The Stars (with SZA)
, Money Trees
, Realest (with Eminem)
, Re-Up
, Up Down (Step & Walk)
, Dance Now (feat. Kenny Mason)
, El Melouk
, Sayrena Ya Donia
, Costa Rica (with Bas & JID feat. Guapdad 4000, Reese LAFLARE, Jace, Mez, Smokepurpp, Buddy & Ski Mask The Slump God)
, Beautiful Catastrophe
, Think
, If We Being Rëal
, DAMNSON
, Big Dawgs
, The Only Thing They Fear Is You
, 交錯
, Thrillin
, Etganen
, Favorite Color Is Blue - John J C Carr Remix
, Favorite Color Is Blue - Tommy Rush Remix
, SUNRISE (Slowed + Reverb)
, Gold Digger
, Skyfall
, Skyfall - Slowed + Reverb
, Reaper
, TIL FURTHER NOTICE (feat. James Blake & 21 Savage)
, Tuyo (Narcos Theme) [Extended Version] - A Netflix Original Series Soundtrack
, Tuyo (Narcos Theme) - A Netflix Original Series Soundtrack
, Get You (feat. Kali Uchis)
, En Kont Ghaly
, Alright
, Let U Go
, paranoia
, Running Up That Hill (A Deal With God)
, you & i
, HIND'S HALL
, PARANOIA
, Yalmidan
, Family Matters
, Not Like Us
, Igual Que Un Ángel (with Peso Pluma)
, meet the grahams
, redrum
, Angel
, Kung Fu
, Cash In Cash Out
, Ultralight Beam
, Pain 1993 (with Playboi Carti)
, ILoveUIHateU
, PAIN
, Push Ups
, Superhero (Heroes & Villains) [with Future & Chris Brown]
, Weakest Link
, Snooze
, Saturn
, Street Fight
, Like That
, Lights Out
, Hello
, Don’t Need You
, As You Are
, Skitzo
, I Don't Wanna
, Forged In Fire (feat. Locksmith, Alandon & Sway Calloway)
, Suicide Squad (feat. Jarren Benton & Locksmith)
, Doomsday Pt. 2 (with Eminem)
, Doomsday (with Juice WRLD & Cordae)
, Shady
, Collard Greens
, Mood Swings
, Venom
, Gorilla
, First Person Shooter (feat. J. Cole)
, Sinners (feat. Thomas LaRosa)
, I'll Get Over You
, Bling-Bang-Bang-Born
, King Kong
, Kolloh Beynafsen
, SICKO MODE
, Klavstrix - SLOWED
, For Narmer (From "Warframe")
, مش حقيقة
, Movement
, King Of The Jungle
, Paris
, Stayin' Alive
, Мой мармеладный (Я не права)
, Walk It Talk It
, Careless Whisper
, Phobia
, Château Gris
, SMOKE (feat. Jasiah)
, BUSINESS MAN (feat. Juicy J)
, GUTS!
, These Days
, Love Is A Long Road
, UR FINAL MESSAGE - Slowed + Reverb
, Twirlanta - Slowed Down Version
, Running Away
, Parking Lot
, The Delicious Last Course
, Ahwak
, Al Bostah
, Batwanes Beek
, PUNK TACTICS
, HOOLIGANG
, Stories of Hope
, JAPAN
, 2 seater - house edit
, need it - slowed + reverb
, Last Things First
, November 9th
, alwan
, Million Cash
, Devil's Work
, INCOMING
, WARNING
, Wana
, Boom (feat. JID)
, Fluxxwave (Lay With Me) - Slowed + Reverb
, Run
, Monster
, Bump Heads
, Trendsetter
, The Good Part
, Have Yourself a Merry Little Christmas
, Voice of no Return
, Strangers
, Titanfall 2: My Pills
, YOUR FINAL MESSAGE
, YOUR FINAL MESSAGE - slowed
, Meet the Frownies
, Lovely Bastards X Meet The Frownies
, Move Your Body - RAIZHELL Remix
, LOVELY BASTARDS
, 9mm
, One Chance
, Lights
, Get Off My Penis!
, Oh Boy (feat. Busta Rhymes)
, Отключаю телефон (Slowed)
, My Song
, STUCK IN A DAZE
, Ditty
, Quiet Storm
, Hey Luv (Anything) (feat. 112)
, Hell on Earth (Front Lines)
, Miganinani
, Outro: Outta Control - Remix
, Bastard
, Check the Rhime
, Shook Ones, Pt. II
, Yonkers
, She
, Goblin
, My Name Is
, Eazy-Duz-It
, Nuthin' But A "G" Thang
, Drop It Like It's Hot
, The Next Episode
, Mockingbird
, Me Against The World
, Mirror Temple - Mirror Magic Mix
, Rainy Season
, Summer Walk
, Enemy (with JID) - from the series Arcane League of Legends
, 777
, All I Need
, Doja
, Hit 'Em Up - Single Version
, Can We Be Free
, Feasting.On.The.Guts.Of.Angels.
, 青のすみか
, Jujutsu Kaisen Opening
, WAKE UP!
, NEON BLADE
, MELTDOWN (feat. Drake)
, Havana (feat. Young Thug)
, Ready to Score
, It Was A Good Day
, Life Letters
, do it right (feat. Aminé)
, West Coast Love
, Bang Bang
, Daylight
, Gasoline
, Ni**as In Paris
, Snowman
, NXSTY BLOOD
, Moth Grinder
, Survival of the Fittest
, Dr0nched In Sw0t
, Bankroll
, Levitating
, Switch Lanes
, Crazy
, WTF!
, Telepatiax (Slowed) - Remix
, Still Hot
, Big Poppa - 2007 Remaster
, Now I'm Up to My Neck with Offers
, Bad Ass Bitches
, Fallen Down
, Phonk Drift
, Toca Toca
, POOR
, Stick Up
, Øfdream: Thelema (Slowed & Bass Boosted)
, AVOID ME
, Hush
, Ur Final Message - Slowed
, Disposable Society
, Until We Die
, SAOKO
, Pray For Me (with Kendrick Lamar)
, Reset Head
, Shamandora
, Hara El Saqueen
, Violence
, Lust
, The Difference
, Never Be Like You
, You & Me - Flume Remix
, Wtf U Mean (feat. Freddie Dredd)
, The Alchemist
, Spinnin
, Stone Cold
, Xxxxxxx
, Lost and Found - live
, El 3asal
, Somebody That I Used To Know
, Riders
, Test & Recognise - Flume Re-work
, PYRO - Extended Mix
, Take Over
, ÁGUA DE BEBER
, Reflections
, Smart Cube
, Glock In My Lap
, Why Not
, Aces
, Purpose
, GHOST!
, Brain Dead
, Awareness
, One and Only
, Good Little Girl
, Set Fire to the Rain
, Limbo
, Disaster
, KILLSHOT
, UNIVERSAL COLLAPSE
, COWBELL WARRIOR!
, ولعانه
, Harbinger
, SPIT IN MY FACE!
, Kick Rocks (feat. Lil Darkie)
, Wrath
, Stunna
, People You Know
, Taste
, Survivor
, Blunts
, Momma I Hit A Lick (feat. Kendrick Lamar)
, Watch It Burn
, m.A.A.d city
, Never
, Pearl Diver
, Learning To Live Without You
, Infamous Kiss
, Drop
, Sing About Me, I'm Dying Of Thirst
, Fragile
, Knife Talk (with 21 Savage ft. Project Pat)
, Play with Fire (feat. Yacht Money) - Extended Mix
, PRINCE OF DARKNESS
, Feel Good Inc.
, Rhinestone Eyes
, dead!
, love nwantiti (feat. Dj Yo! & AX'EL) - Remix
, RAVEN
, ili
, Carti
, Do You?
, Jupiter
, Hot One
, The Hills X Creepin X The Color Violet
, belong with her.
, im all alone
, Are You Okay?
, Step Back!
, BABYDOLL
, The Perfect Girl - Arabic Version
, LOST
, SLAUGHTER HOUSE
, WRATH
, Gettin' Jiggy Wit It
, Sag My Pants
, Not Like You
, Stan - Instrumental
, Say Yeah
, DEMONS IN MY SOUL
, False Alarm
, DIP
, Lucky You (feat. Joyner Lucas)
, Bruuuh (with Denzel Curry) - Remix
, Crack Sandwich
, Off Deez (with J. Cole)
, Kaine / Salvation
, Chuck Taylor
, Living Life, In The Night - slowed
, Sick of U (with Oliver Tree)
, Life Goes On
, WORTH NOTHING - Fast & Furious: Drift Tape/Phonk Vol 1
, Song of the Ancients / Devola
, DEMONS IN MY SOUL - Slowed
, Snow in Summer
, Violet
, Crystals
, telepatía
, BOW
, Minnie The Moocher
, Memphis Doom
, Fuck You
, imma
, nursery
, C'est La Vie (with bbno$ & Rich Brian)
, edamame
, VILLAIN
, Bleed
, FROZEN
, Rise Up
, 名探偵コナン メイン・テーマ - 世紀末ヴァージョン
, Breathe (In the Air)
, Through and Through
, i love being with you
, this girl
, Jolyne Theme (from "Stone Ocean")
, The Ballad of G and X // Interlude
, Psycho
, The One
, Damned
, Lullaby Of A Deadman
, Rising Tide
, WARDOGZ
, OPEN WOUNDS
, COURAGE
, Six Speed
, Beautiful Catastrophe - Instrumental Version
, Beast Unleashed 4
, Ghostface Killers
, My Final Song
, Reflections of the Mind
, 999
, IMMORTAL
, Can't Say
, Radiator
, Hustle
, Demons (feat. Caskey & JP)
, From The D 2 The LBC (with Snoop Dogg)
, You Know How We Do It
, Pearl Diver
, Liquid Smooth
, Madad Ya Rasoul Allah
, prolly my spookiest beat (slowed + reverb)
, Queen of Pain
, Twilight
, vendetta!
, Downstairs
, Jump in the Line
, Living Life, In The Night
, OLD GENESIS
, Ultimatum
, Bang!
, World's Smallest Violin
, Caffeine
, Insane
, Think
, i'm tired of feeling this way
, Break
, GAZ
, Wellerman - Sea Shanty
, Leave Her Johnny
, Drunken Sailor
, Loveyou
, Sahara
, Keraunos
, PROPHECY
, PRINCE OF DARKNESS - Slowed + Reverb
, ADRENALIN
, Imperial
, Terrorwave
, Devil Ride
, Keraunos Killer
, Murder In My Mind
, PURE MONSTROSITY
, Disaster
, Override
, Chase
, MIDNIGHT SHIFT
, Phonky Town
, Dancing in My Room
, Thelema
, Bloom
, Amend
, Thanks Officer
, Need You
, Night Hawk
, Panic Room
, Elevator
, Miki The Witch
, Weeble Wobble
, Numb
, BREAKSH!T
, Stupid
, Crossfire
, Judgement
, Smells Blood
, Tick Tick Boom (feat. BygTwo3)
, Freak
, Cheatcode
, Mon Soleil - from "Emily in Paris" Soundtrack
, Dance in the Dark
, Surround Sound (feat. 21 Savage & Baby Tate)
, Offended
, GP4
, Kill EVERYBODY
, Gospel (with Eminem)
, Overkill
, Killshot
, 40 Cal
, Slap!
, The Way (Instrumental)
, Scary Garry
, Close - Brooks Remix
, Stardust Crusaders
, Killer
, Uragirimonono Requiem - Giorno Ver.
, Uragirimonono Requiem - English Ver.
, Traitor's Requiem
, Jolyne's Theme / Stone Ocean (but it's lofi hiphop)
, il vento d'oro
, Dirty Little Animals (From the series Arcane League of Legends)
, Don't Bring Me Down
, Pigs In The Sky VIP (feat. Arrested Youth)
, Monster
, PATCHWERK
, Burn It All Down
, Burn (feat. Locksmith & Apathy)
, Everyday Normal Guy 2
, Josuke Theme - Epic Version (Diamond is Unbreakable)
, Diamond is unbreakable - Main Theme
, Yoshikage Kira Theme
, Amnesia
, Tell Me
, So High
, IT G MA REMIX (feat. A$AP Ferg, Father, Dumbfoundead, Waka Flocka Flame)
, The Hanging Tree
, Amber Alert
, Dreamland
, Object
, King Of The Damned
, Ping Pong Party
, Ice Cream
, dead!
, Behind My Eyes - Vanic Remix
, Distance - Volac Remix
, Lacrimosa
, Exterminate
, Seven Nation Army
, Banana Boat (Day-O)
, Unstoppable
, Anxious
, Float Away
, DETECTIVE CONAN MAIN THEME DEEP AZURE ver.
, Need not to know．
, 記憶喪失 (影)
, 名探偵コナン メイン・テーマ - 暗殺者ヴァージョン
, ターゲット サスペンス C
, 名探偵コナン メイン・テ－マ - 標的ヴァージョン
, 対決のテーマ - 摩天楼ヴァージョン
, 陰謀 - 摩天楼ヴァージョン
, 爆破犯人のテーマ
, Lunatic
, Time of my Life
, Wings
, Ricochet
, 最恐
, Do I Wanna Know?
, Inappropriate (Freeverse)
, Darkside
, Rain (from The Suicide Squad)
, Blood // Water
, Dirty
, Uebok Gotta Run
, Waiting
, Collapse
, Happy - From "Despicable Me 2"
, Blurred Lines
, Like A G6
, Inside (feat. Cynthia Erivo)
, 13
, Again (feat. XXXTENTACION)
, All Eyes On Me
, Envious
, Killer: Yoshikage Kira's Theme (From"Jo Jo's Bizarre Adventure Diamond Is Unbreakable")
, Jotaros Theme (From "Jo Jo's Bizarre Adventure: Stardust Crusaders")
, Time Warp
, Appetite for Destruction
, Work
, Talk Dat Shit To Me
, Majesty
, Royalty
, Killer (feat. Jack Harlow & Cordae) - Remix
, Lone Wolf
, Riptide
, 5 A.M.
, I Don't Trust Nobody
, Feeling Good
, Heartburn
, Gangsta's Paradise
, Beat It
, Billie Jean
, Trisha's Lullaby (Soundtrack from the Anime "Fullmetal Alchemist" Brotherhood)
, Sorrowful Stone (Soundtrack from the Anime "Fullmetal Alchemist" Brotherhood)
, Lost in the Fire (feat. The Weeknd)
, Bang It To The Curb
, When the Credits Roll
, Destroid 8 Annihilate
, Sirens Over Paris
, Wicked
, Cool Friends - Murtagh & Veschell Remix
, HYPE
, Vitality
, Clash
, The Ecstasy of Gold - L'Estasi Dell'oro
, Knockin'
, Riddle
, King / Ghost In A Song
, CLOUDS
, Move On
, Everytime
, Ricochet on My Mind
, Astronaut In The Ocean (Remix) - feat. G-Eazy & DDG
, Empty Place
, Grateful
, Bloody Stream
, Addicted
, whatdoyoudo?
, You & Jennifer
, Get Stüpid
, Let There Be Drums
, Internet Rap
, Time
, Boushret Kheir
, High Frequency
, Close To Hell
, Ultimate
, Young Shahrukh
, Anime Thighs
, The Ketchup Song (Aserejé) - Spanglish Version
, Heist
, Barracuda
, DAYLIGHT
, JINN
, Keep You
, I Stand On That
, Automatic
, Astronaut In The Ocean
, Facebooky
, Paradise
, Papa Told Me
, One Day (Hayeegy El Youm)
, Already Gone
, Runaway
, Bulletproof
, Battle Royale feat. Panther - VIP Mix
, RUNAWAY
, MoneyOnMyMind (feat. Absofacto)
, STOP!
, Happy Endings (feat. iann dior and UPSAHL)
, Cigarettes Are Gross
, Till It's Done
, Bang!
, No Twerk feat. Panther X Odalisk - Original Mix
, B.Y.L
, Weight of the World the End of YoRHa
, The Tower
, Emil (Despair)
, Rebirth & Hope
, Dark Colossus (Kaiju)
, Pascal
, The Color of Depression
, City Ruins (Rays of Light)
, Pressure (feat. Tove Lo)
, Sumthin' Light
, Riot
, Bounce
, One Take
, No Words - Skit
, No Words 2 (Skit)
, Run It
, Warriors
, Zeus (feat. White Gold)
, Killer
, Gnat
, Alfred’s Theme
, The Last of Us
, Energy
, Beast Mode
, Mr. Sandman
, Faceless
, Smack That
, Numb
, بنت متناكة
, Bury the Light
, Stronger
, Freeverse 4
, Freeverse 5
, Diablo
, Wattson
, Wraith
, Pathfinder
, Mirage
, Octane
, Freeverse 3
, Wish You'd Make Me Cry
, Next
, What They Want?
, Alphabet Insanity 2
, Update
, Hello
, Fly Me to the Moon
, Someone Like You
, Moonlight
, Isolate
, Evil
, Zenith
, Crash & Burn
, Bad Habits
, Drugs
, Overtime
, Witch Doctor
, As We Are (feat. John Nonny)
, On Top (feat. Jelly Roll & Rittz)
, People I Don't Like
, Standby
, Drugs (feat. Two Feet)
, 12345SEX
, Habits (Stay High)
, like that
, She's Got a Gun
, Don't Stop
, Freeverse
, Closed Off
, Good Thing
, Okay
, Water Fountain
, Let Me Down Slowly
, Alright
, No Hype
, I Wouldn't Do That
, Twisted
, Leather Face (feat. King Gordy & Lazarus)
, Somnus
, ENTERFEARENCE (Intro 3)
, Bitch Slap
, Elephants
, Bass (feat. Tech N9ne & Hopsin)
, Hammer - Travis Barker Remix
, Talk (feat. Tech N9ne & Devvon Terrell)
, On the Bible
, THE BADDEST
, Dysfunctional
, Wack Ass Rappers
, Ill Mind of Hopsin 9
, Only You Freestyle
, Don't Rush (feat. Headie One)
, Put Your Hands Where My Eyes Could See (feat. Jamal)
, I Know What You Want (feat. Flipmode Squad)
, Rip & Tear
, Bfg Division
, Young & Alive - Bazzi vs. Haywyre Remix
, Never Count On Me
, Hellwalker
, At Doom's Gate
, Now I'm Forever
, Top Of The World
, DadBod
, Chloraseptic (feat. 2 Chainz & Phresher) - Remix
, The Adventures of Moon Man & Slim Shady (with Eminem)
, Let Down (feat. Futuristic)
, Opportunities
, Do You Don't You
, Meaning
, I Remember
, Chase Pop
, Easily
, At the End
, No Pressure Intro
, Perfect
, Ber Zer Ker
, YouTube Cypher, Vol. 2
, Run
, KAMIKAZE
, Darkside
, Don't Rush (feat. Busta Rhymes)
, Hurricane
, Break Ya Neck
, The Path
, Honeymoon
, Look At Me Now (feat. Lil' Wayne & Busta Rhymes)
, Infinite
, Your Eyes
, Morning View
, Fantasy
, Sunkissed
, Lost in You
, Kumbaya
, Jackknife
, Plain Jane REMIX (feat. Nicki Minaj)
, My House
, Heart Shaped Box
, Should've Started
, Rendezvous
, Sign
, Give Me Your Love
, Moi
, Going Off
, All Night
, Get Lucky (Radio Edit) [feat. Pharrell Williams and Nile Rodgers]
, Beast Unleashed 2
, Through It All
, See Me Drop
, On Repeat
, Don't Do It
, Beast Unleashed 3
, Get Like Me
, Addicted
, What If
, In Your Brain
, On Our Way
, Numb
, Death to Mumble Rap
, Crash
, JOKER
, Alphabet Insanity
, Space Cadet (feat. Gunna)
, DICTATOR
, Can't Be Saved
, I Will (feat. KXNG Crooked, Royce Da 5'9" & Joell Ortiz)
, Ocean's Roar (COE Remix)
, Black (feat. A$AP Ferg)
, Happy Together
, I Feel Like I'm Drowning
, Fi Ishk El Banat
, Boss Bitch
, Sugar
, Souvenir
, Giorno's Theme
, Friend Like Me
, Somnus - Instrumental Version
, Safe Haven
, Beast Unleashed
, Let You Down
, Don't Sleep
, Freak (feat. REI AMI)
, GDFR (feat. Sage the Gemini & Lookas)
, ¿ (feat. Halsey)
, Afraid of the Dark
, Hero's Come Back!!（第1話〜第30話）
, Starbound
, Reverie
, Take Me Down
, Joke's On You
, Lean On
, Caterpillar (feat. Eminem & King Green)
, JOLT
, Little Poor Me - Vosai Remix
, Spagonia - Day
, Overnight Celebrity (feat. Miri Ben-Ari)
, Symphony
, No Scrubs
, The Motto
, Vertigo
, Ber Zer Ker - Rob Gasser Remix
, Get Low
, Waiting
, You Should've Known
, Ni**a Ni**a Ni**a
, I.F.L.Y.
, My Oh My (feat. DaBaby)
, Revenge
, Ill Mind of Hopsin 8
, She Cheated Again
, Lock It Up (feat. Anderson .Paak)
, Liar
, Girei (Pains Theme) (From " Naruto Shippuden Girei")
, Ah Yasmarany
, Abo El Taaiyya
, You Gon’ Learn (feat. Royce Da 5'9" & White Gold)
, Those Kinda Nights (feat. Ed Sheeran)
, Darkness
, Unaccommodating (feat. Young M.A)
, Godzilla (feat. Juice WRLD)
, Farewell
, Ill Mind of Hopsin 5
, Unity
, Fly Away
, Stronger
, Turn It Up
, Heroes
, Superlife
, Houndin
, Never Seen the Rain
, Memories
, Circles
, hot girl bummer
, ADHD
, Am I a Psycho? (feat. B.o.B. and Hopsin)
, Still D.R.E.
, Take That (Bonus Track)
, Aiwa
, The Mob
, First of the Year (Equinox)
, Which Direction?
, Coming Down
, OCD (with Dwn2earth)
, Sucker for Pain (with Wiz Khalifa, Imagine Dragons, Logic & Ty Dolla $ign feat. X Ambassadors)
, See You Again (feat. Charlie Puth)
, Intro
, Favorite Color Is Blue
, Lose Yourself
, Starboy
, Start a Riot
, No Glory (feat. M.I.M.E & Drama B)
, Too Alive
, Living Hell (feat. Blvkstn)
, War Zone
, The City
, Warriors
, Pretty's on the Inside
, Take Me To Church
, Brooklyn Love
, Under Pressure
, Phoenix (Carpenter Brut Remix)
, The Real Slim Shady
, Without Me
, WHY
, Way down We Go
, TURBO
, Silver Bullet
, Hokage's Funeral (From 'Naruto')
, False Alarm
, Still D.R.E.
, Naruto's Daily Life (From 'Naruto')
, Evil (From 'Naruto')
, ブルーバード
, Mamacita (feat. Wizkid)
, Forgot About Dre
, Midwest Choppers
, Midwest Choppers 2
, Break Ya Neck
, Rap God
, Till I Collapse
, NO
, Me Too
, Jungle Fury
, What A Wonderful World
, I Got You (I Feel Good)
, Hurts Like This
, Drop It Like It's Hot
, Afterglow - Official Holi Festival of Colours Anthem 2017
, Gang Related
, Blood In The Cut
, Make Me Fade
, Change
, Purple Lamborghini (with Rick Ross)
, Money In The Grave (Drake ft. Rick Ross)
, When I Grow Up
, Time - Edit
, New Game
, Power Trip
, Nock Em
, Bitter World
, Enslaved
, Devil
, Ride 4 U - Barren Gates Remix
, Code Red
, Move Slow
, Me, Myself & I
, I Have Questions
, Awaken
, Waiting For You
, Young Jesus
, Ensay
, Leave Me Alone
, The Edge
, I Miss The Days
, The Search
, In Da Club
, Candy Shop
, P.I.M.P.
, Dancin (feat. Luvli) - Krono Remix
, Stainless
, EDI's
, Dirty Bass
, Five More Hours
, The Illest
, Oops!...I Did It Again
, Higher
, HUMBLE.
, do re mi
, Isis
, Think
, Taste (feat. Offset)
, Speedom (Wwc2)
, Like I Ain't
, Without Me
, Nightmare
, Goosebumps
, I Love
, Crimson Cloud - Game Edit
, Devil Trigger - Game Edit
, I Don't Die
, Nice Colors
, Homicide
, When I Was Young
, Stranger Things
, Kream (feat. Tyga)
, Chun-nan - Night
, Ultimately
, Fantasy
, Surface
, Secret - does not apply
, all the kids are depressed
, Writing's On The Wall - From "Spectre" Soundtrack
, Go Fuck Yourself
, Worldwide Choppers (feat. Ceza, JL B.Hood, Uso, Yelawolf, Twista, Busta Rhymes, D-Loc and Twisted Insane)
, Hood Go Crazy
, I Get It Now
, Get Off Me
, No Gun Control
, Confessions of a Dangerous Mind
, What's Up Danger (with Black Caviar)
, Sunflower - Spider-Man: Into the Spider-Verse
, Scared of the Dark (feat. XXXTENTACION)
, 1%
, Happy - From "Despicable Me 2"
, Come Get It Bae
, Shake That
, 44 More
, Keanu Reeves
, The FPS Rap Battle
, Warriors
, 1-800-273-8255
, My Humps
, Crying in the Club
, OMG (feat. Quavo)
, Heathens
, The Motto
, Failure
, The Ringer
, XO Tour Llif3
, Bangarang (feat. Sirah)
, Cloud City
, Buck
, Stomp
, Fall
, Override
, 7 Years
, Vault
, RAMPAGE
, Rumble
, Closer
, Bounce Back
, Jungle Jane
, Werk
, Turn off the Lights (feat. Alexis Roberts)
, Set Free
, Rapture
, Talking Body - KREAM Remix
, Animals
, Natural
, RISE - Remix
, I Got It (feat. Brooke Candy, CupcakKe and Pabllo Vittar)
, Sriracha
, Castle
, SAD!
, Wake Up (feat. Jessi Mason)
, Are We Still Young (feat. Jessi Mason)
, You Don't Know Me (In the Style of Jax Jones (feat. Raye))
, Without You (feat. Victoria Zaro)
, POP/STARS
, Better With Time
, Talking Body
, Venus
, Fuel
}


list 2 {
    1%.mp3
1-800-273-8255.mp3
12345SEX.mp3
13.mp3
2 seater - house edit.mp3     
31 Freestyle.mp3
40 Cal.mp3
44 More.mp3
5 A.M..mp3
777.mp3
999.mp3
9mm.mp3
Abo El Taaiyya.mp3
Aces.mp3
Addicted (1).mp3
Addicted.mp3
ADHD.mp3
ADRENALIN.mp3
After LIKE.mp3
Again (feat. XXXTENTACION).mp3
Ah Yasmarany.mp3
Ahwak.mp3
Aiwa.mp3
Al Bostah.mp3
Alfred’s Theme.mp3
All Eyes On Me.mp3
All I Need.mp3
all the kids are depressed.mp3
All The Stars (with SZA).mp3
Alphabet Insanity 2.mp3
Already Gone.mp3
Alright (2).mp3
Alright.mp3
alwan.mp3
Am I a Psycho_ (feat. B.o.B. and Hopsin).mp3
Amber Alert.mp3
Amend.mp3
Amnesia.mp3
Angel.mp3
Animals.mp3
Anxious.mp3
Appetite for Destruction.mp3
APT..mp3
Are We Still Young (feat. Jessi Mason).mp3
Are You Okay_.mp3
As We Are (feat. John Nonny).mp3
As You Are.mp3
Astronaut In The Ocean (Remix) - feat. G-Eazy & DDG.mp3
Astronaut In The Ocean.mp3
At Doom's Gate.mp3
At the End.mp3
Automatic.mp3
AVOID ME.mp3
Awareness.mp3
B.Y.L.mp3
BABYDOLL.mp3
Back On My BS.mp3
Bad Ass Bitches.mp3
Bad Habits.mp3
Banana Boat (Day-O).mp3
Bang Bang.mp3
Bang!.mp3
Bangarang (feat. Sirah).mp3
Bankroll.mp3
Bass (feat. Tech N9ne & Hopsin).mp3
Bastard.mp3
Batwanes Beek.mp3
Beast Mode.mp3
Beast Unleashed 4.mp3
Beat It.mp3
Beautiful Catastrophe - Instrumental Version.mp3
Beautiful Catastrophe.mp3
Behind My Eyes - Vanic Remix.mp3
belong with her.mp3
Ber Zer Ker - Rob Gasser Remix.mp3
Ber Zer Ker.mp3
Better With Time.mp3
Bfg Division.mp3
Big Dawgs.mp3
Big Poppa - 2007 Remaster.mp3
Billie Jean.mp3
Bitch Slap.mp3
Bitter World.mp3
Bleed.mp3
Bling-Bang-Bang-Born.mp3
Blood Sweat & Tears (from the series Arcane League of Legends).mp3
Blood __ Water.mp3
Bloody Stream.mp3
Bloom.mp3
Blunts.mp3
Blurred Lines.mp3
Boom (feat. JID).mp3
Bounce Back.mp3
Bounce.mp3
BOW.mp3
Brain Dead.mp3
Break.mp3
BREAKSH!T.mp3
Breathe (In the Air).mp3
Brooklyn Love.mp3
Bruuuh (with Denzel Curry) - Remix.mp3
Buck.mp3
Bump Heads.mp3
Burn (feat. Locksmith & Apathy).mp3
Burn It All Down.mp3
Bury Me Face Down.mp3
Bury the Light.mp3
C'est La Vie (with bbno$ & Rich Brian).mp3
Caffeine.mp3
Can We Be Free.mp3
Can't Be Saved.mp3
Can't Say.mp3
Candy Shop.mp3
Careless Whisper.mp3
Carti.mp3
Cash In Cash Out.mp3
Castle.mp3
Caterpillar (feat. Eminem & King Green).mp3
Change.mp3
Chase Pop.mp3
Chase.mp3
Cheatcode.mp3
Check the Rhime.mp3
Chloraseptic (feat. 2 Chainz & Phresher) - Remix.mp3
Chuck Taylor.mp3
Chun-nan - Night.mp3
Château Gris.mp3
Cigarettes Are Gross.mp3
City Ruins (Rays of Light).mp3
Clint Eastwood.mp3
Close - Brooks Remix.mp3
Closed Off.mp3
Closer.mp3
Cloud City.mp3
CLOUDS.mp3
Code Red.mp3
Collapse.mp3
Collard Greens.mp3
Come Get It Bae.mp3
Confessions of a Dangerous Mind.mp3
Cool Friends - Murtagh & Veschell Remix.mp3
Costa Rica (with Bas & JID feat. Guapdad 4000, Reese LAFLARE, Jace, Mez, Smokepurpp, Buddy & Ski Mask The Slump God).mp3
COURAGE.mp3
COWBELL WARRIOR!.mp3
Crack Sandwich.mp3
Crash & Burn.mp3
Crash.mp3
Crazy In Love (feat. JAY-Z).mp3
Crazy.mp3
Crimson Cloud - Game Edit.mp3
Crossfire.mp3
Crying in the Club.mp3
Crystals.mp3
Cupid - Twin Version.mp3
DadBod.mp3
Damned.mp3
DAMNSON.mp3
Dance in the Dark.mp3
Dance Now (feat. Kenny Mason).mp3
Dancin (feat. Luvli) - Krono Remix.mp3
Dancing in My Room.mp3
Dark Crow (TV size).mp3
Dark Crow.mp3
Darkness.mp3
Darkside.mp3
Daylight.mp3
dead!.mp3
Demons (feat. Caskey & JP).mp3
DEMONS IN MY SOUL - Slowed.mp3
DEMONS IN MY SOUL.mp3
Destroid 8 Annihilate.mp3
DETECTIVE CONAN MAIN THEME DEEP AZURE ver..mp3
Devil Ride.mp3
Devil Trigger - Game Edit.mp3
Devil's Work.mp3
Devil.mp3
Diablo.mp3
Diamond is unbreakable - Main Theme.mp3
DICTATOR.mp3
Die Young.mp3
DIP.mp3
Dirty Bass.mp3
Dirty Little Animals (From the series Arcane League of Legends).mp3
Dirty.mp3
Disaster.mp3
Disposable Society.mp3
Distance - Volac Remix.mp3
Ditty.mp3
Do I Wanna Know_.mp3
do it right (feat. Aminé).mp3
do re mi.mp3
Do You Don't You.mp3
Do You_.mp3
Doja.mp3
Don't Bring Me Down.mp3
Don't Rush (feat. Headie One).mp3
Don't Stop.mp3
Don’t Need You.mp3
Doomsday (with Juice WRLD & Cordae).mp3
Doomsday Pt. 2 (with Eminem).mp3
Downstairs.mp3
Dr0nched In Sw0t.mp3
Dreamland.mp3
Drop It Like It's Hot.mp3
Drop.mp3
Drugs (feat. Two Feet).mp3
Drugs.mp3
Drunken Sailor.mp3
Dysfunctional.mp3
Easily.mp3
Eazy-Duz-It.mp3
edamame.mp3
EDI's.mp3
Ekhwaty.mp3
El 3asal.mp3
El Melouk.mp3
Elephants.mp3
Elevator.mp3
Empty Place.mp3
En Kont Ghaly.mp3
Enemy (with JID) - from the series Arcane League of Legends.mp3
Ensay.mp3
ENTERFEARENCE (Intro 3).mp3
Envious.mp3
Etganen.mp3
Everyday Normal Guy 2.mp3
Everytime.mp3
Evil.mp3
Facebooky.mp3
Faceless.mp3
Failure.mp3
Fall.mp3
Fallen Down.mp3
False Alarm.mp3
Family Matters.mp3
family ties (with Kendrick Lamar).mp3
Fantasy.mp3
Farewell.mp3
Favorite Color Is Blue - John J C Carr Remix.mp3
Favorite Color Is Blue - Tommy Rush Remix.mp3
Feasting.On.The.Guts.Of.Angels..mp3
Feel Good Inc Remix.mp3
Feel Good Inc..mp3
Feeling Good.mp3
First Person Shooter (feat. J. Cole).mp3
Five More Hours.mp3
Float Away.mp3
Fluxxwave (Lay With Me) - Slowed + Reverb.mp3
Fly Away.mp3
Fly Me to the Moon.mp3
For Narmer (From _Warframe_).mp3
Forged In Fire (feat. Locksmith, Alandon & Sway Calloway).mp3
Forgot About Dre.mp3
Fortress of Lies.mp3
Fragile.mp3
Freak (feat. REI AMI).mp3
Freak.mp3
Freeverse 3.mp3
Freeverse 4.mp3
Freeverse 5.mp3
Freeverse.mp3
From The D 2 The LBC (with Snoop Dogg).mp3
From The Start.mp3
FROZEN.mp3
Fuck You.mp3
Fuel.mp3
Gangsta's Paradise.mp3
Gasoline.mp3
GAZ.mp3
Get Like Me.mp3
Get Low.mp3
Get Lucky (Radio Edit) [feat. Pharrell Williams and Nile Rodgers].mp3
Get Off Me.mp3
Get Off My Penis!.mp3
Get You (feat. Kali Uchis).mp3
Gettin' Jiggy Wit It.mp3
GHOST!.mp3
Ghostface Killers.mp3
Girei (Pains Theme) (From _ Naruto Shippuden Girei_).mp3
Glock In My Lap.mp3
Gnat.mp3
Go Fuck Yourself.mp3
Goblin.mp3
Godzilla (feat. Juice WRLD).mp3
Gold Digger.mp3
Good Little Girl.mp3
Good Thing.mp3
Goosebumps.mp3
Gorilla.mp3
Gospel (with Eminem).mp3
GP4.mp3
GUTS!.mp3
Hammer - Travis Barker Remix.mp3
Happy - From _Despicable Me 2_ .mp3
Hara El Saqueen.mp3
Harbinger.mp3
Havana (feat. Young Thug).mp3
Have Yourself a Merry Little Christmas.mp3
Heartburn.mp3
Heathens.mp3
Hell on Earth (Front Lines).mp3
Hello.mp3
Hellwalker.mp3
Hero's Come Back!!（第1話〜第30話）.mp3
Hey Luv (Anything) (feat. 112).mp3
HIND'S HALL.mp3
Hit 'Em Up - Single Version.mp3
Homicide.mp3
Honeymoon.mp3
Hood Go Crazy.mp3
HOOLIGANG.mp3
hot girl bummer.mp3
Hot One.mp3
Houndin.mp3
HUMBLE..mp3
Hush.mp3
Hustle.mp3
HYPE.mp3
I Don't Die.mp3
I Don't Trust Nobody.mp3
I Don't Wanna.mp3
I Get It Now.mp3
I Got It (feat. Brooke Candy, CupcakKe and Pabllo Vittar).mp3
I Got You (I Feel Good).mp3
I Know What You Want (feat. Flipmode Squad).mp3
i love being with you.mp3
I Love.mp3
I Miss The Days.mp3
I Remember.mp3
I Stand On That.mp3
I Will (feat. KXNG Crooked, Royce Da 5'9_ & Joell Ortiz).mp3
I'll Get Over You.mp3
I'm In Love With a Monster.mp3
i'm tired of feeling this way.mp3
I.F.L.Y..mp3
Ice Cream.mp3
If We Being Rëal.mp3
Igual Que Un Ángel (with Peso Pluma).mp3
il vento d'oro.mp3
ili.mp3
Ill Mind of Hopsin 5.mp3
Ill Mind of Hopsin 8.mp3
Ill Mind of Hopsin 9.mp3
ILoveUIHateU.mp3
im all alone.mp3
imma.mp3
IMMORTAL.mp3
Imperial.mp3
In Da Club.mp3
Inappropriate (Freeverse).mp3
INCOMING.mp3
Infamous Kiss.mp3
Infinite.mp3
Insane.mp3
Inside (feat. Cynthia Erivo).mp3
Isis.mp3
Isolate.mp3
IT G MA REMIX (feat. A$AP Ferg, Father, Dumbfoundead, Waka Flocka Flame).mp3
It Was A Good Day.mp3
JAPAN.mp3
JINN.mp3
Jolyne Theme (from _Stone Ocean_).mp3
Jolyne's Theme _ Stone Ocean (but it's lofi hiphop).mp3
Josuke Theme - Epic Version (Diamond is Unbreakable).mp3
Jotaros Theme (From _Jo Jo's Bizarre Adventure_ Stardust Crusaders_).mp3
Judgement.mp3
Jujutsu Kaisen Opening.mp3
Jump in the Line.mp3
Jungle Jane.mp3
Jupiter.mp3
Just the Two of Us.mp3
Kaine _ Salvation.mp3
KAMIKAZE.mp3
Keanu Reeves.mp3
Keep You.mp3
Keraunos Killer.mp3
Keraunos.mp3
Kick Rocks (feat. Lil Darkie).mp3
Kill EVERYBODY.mp3
Killer (feat. Jack Harlow & Cordae) - Remix.mp3
Killer.mp3
Killer_ Yoshikage Kira's Theme (From_Jo Jo's Bizarre Adventure Diamond Is Unbreakable_).mp3    
Killshot (1).mp3
KILLSHOT.mp3
King Kong.mp3
King Of The Damned.mp3
King Of The Jungle.mp3
King _ Ghost In A Song.mp3
Klavstrix - SLOWED.mp3
Knife Talk (with 21 Savage ft. Project Pat).mp3
Knockin'.mp3
Kolloh Beynafsen.mp3
Kream (feat. Tyga).mp3
Kung Fu.mp3
Laa.mp3
Lacrimosa.mp3
Last Things First.mp3
Learning To Live Without You.mp3
Leather Face (feat. King Gordy & Lazarus).mp3
Leave Her Johnny.mp3
Leave Me Alone.mp3
Leih Beydary Keda.mp3
Let Down (feat. Futuristic).mp3
Let Me Down Slowly.mp3
Let U Go.mp3
Levitating.mp3
Liar.mp3
Life Goes On.mp3
Life Letters.mp3
Lights Out.mp3
Lights.mp3
Like A G6.mp3
Like I Ain't.mp3
Like My Shit.mp3
like that (1).mp3
Like That.mp3
Limbo.mp3
Liquid Smooth.mp3
Living Life, In The Night - slowed.mp3
Living Life, In The Night.mp3
Lock It Up (feat. Anderson .Paak).mp3
Lone Wolf.mp3
Lost and Found - live.mp3
LOST.mp3
Love Is A Long Road.mp3
love nwantiti (feat. Dj Yo! & AX'EL) - Remix.mp3
Lovely Bastards X Meet The Frownies.mp3
LOVELY BASTARDS.mp3
Loveyou.mp3
Lucky You (feat. Joyner Lucas).mp3
Lullaby Of A Deadman.mp3
Lunatic.mp3
Lust.mp3
luther (with sza).mp3
m.A.A.d city.mp3
Madad Ya Rasoul Allah.mp3
Magnetic.mp3
Majesty.mp3
Malatanghulu.mp3
Mamacita (feat. Wizkid).mp3
Me Against The World.mp3
Me, Myself & I.mp3
Meaning.mp3
meet the grahams.mp3
MELTDOWN (feat. Drake).mp3
Memphis Doom.mp3
MIDNIGHT SHIFT.mp3
Miganinani.mp3
Miki The Witch.mp3
Million Cash.mp3
Minnie The Moocher.mp3
Mirage.mp3
Mirror Temple - Mirror Magic Mix.mp3
Mockingbird.mp3
Moi.mp3
Momma I Hit A Lick (feat. Kendrick Lamar).mp3
Mon Soleil - from _Emily in Paris_ Soundtrack.mp3
Money In The Grave (Drake ft. Rick Ross).mp3
Money Trees.mp3
Monster (1).mp3
Monster.mp3
Mood Swings.mp3
Moonlight.mp3
Moral of the Story.mp3
Moth Grinder.mp3
Move On.mp3
Move Your Body - RAIZHELL Remix.mp3
Movement.mp3
Mr. Sandman.mp3
Murder In My Mind.mp3
Murdergram Deux (feat. Eminem).mp3
My Final Song.mp3
My House.mp3
My Humps.mp3
My Name Is.mp3
My Oh My (feat. DaBaby).mp3
My Song.mp3
Natural.mp3
need it - slowed + reverb.mp3
Need not to know．.mp3
Need You.mp3
NEON BLADE.mp3
Never Be Like You.mp3
Never Count On Me.mp3
Never.mp3
New Game.mp3
Next.mp3
Nice Colors.mp3
Night Hawk.mp3
Nightmare.mp3
Ni__a Ni__a Ni__a.mp3
Ni__as In Paris.mp3
No Gun Control.mp3
No Hype.mp3
No Pressure Intro.mp3
No Words - Skit.mp3
No Words 2 (Skit).mp3
Not Like Us.mp3
Not Like You.mp3
November 9th.mp3
Now I'm Forever.mp3
Now I'm Up to My Neck with Offers.mp3
Numb.mp3
nursery.mp3
Nuthin' But A _G_ Thang.mp3
NXSTY BLOOD.mp3
Object.mp3
Octane.mp3
Off Deez (with J. Cole).mp3
Offended.mp3
Oh Boy (feat. Busta Rhymes).mp3
Okay.mp3
OLD GENESIS.mp3
OMG (feat. Quavo).mp3
On the Bible.mp3
On Top (feat. Jelly Roll & Rittz).mp3
One and Only.mp3
One Chance.mp3
One Day (Hayeegy El Youm).mp3
One Take.mp3
Only You Freestyle.mp3
Oops!...I Did It Again.mp3
OPEN WOUNDS.mp3
Opportunities.mp3
Outro_ Outta Control - Remix.mp3
Overkill.mp3
Overnight Celebrity (feat. Miri Ben-Ari).mp3
Override (2).mp3
Override.mp3
Overtime.mp3
Pain 1993 (with Playboi Carti).mp3
PAIN.mp3
Panic Room.mp3
Paradise.mp3
PARANOIA (1).mp3
paranoia.mp3
Paris.mp3
Parking Lot.mp3
PATCHWERK.mp3
Pathfinder.mp3
Peaceful Sleep.mp3
Pearl Diver.mp3
People I Don't Like.mp3
People You Know.mp3
Perfect.mp3
Phobia.mp3
Phonk Drift.mp3
Phonky Town.mp3
Pigs In The Sky VIP (feat. Arrested Youth).mp3
Ping Pong Party.mp3
Play with Fire (feat. Yacht Money) - Extended Mix.mp3
POOR.mp3
POP_STARS.mp3
Pray For Me (with Kendrick Lamar).mp3
Pressure (feat. Dr. Dre & K.A.A.N.).mp3
Pressure (feat. Tove Lo).mp3
pressure - slowed + reverb.mp3
Pressure.mp3
Pretty's on the Inside.mp3
PRINCE OF DARKNESS - Slowed + Reverb.mp3
PRINCE OF DARKNESS.mp3
prolly my spookiest beat (slowed + reverb).mp3
PROPHECY.mp3
Psycho.mp3
PUNK TACTICS.mp3
PURE MONSTROSITY.mp3
Purple Lamborghini (with Rick Ross).mp3
Purpose.mp3
Push Ups.mp3
Put Your Hands Where My Eyes Could See (feat. Jamal).mp3
PYRO - Extended Mix.mp3
Queen of Pain.mp3
Quiet Storm.mp3
Radiator.mp3
Rain (from The Suicide Squad).mp3
Rainy Season.mp3
Raise your flag.mp3
RAMPAGE.mp3
Rapture.mp3
RAVEN.mp3
Re-Up.mp3
Realest (with Eminem).mp3
Reaper.mp3
redrum.mp3
Reflections of the Mind.mp3
Reflections.mp3
reincarnated.mp3
Rendezvous.mp3
Reset Head.mp3
Return of the Tres.mp3
Revenge.mp3
Rhinestone Eyes.mp3
Ricochet (1).mp3
Ricochet on My Mind.mp3
Ricochet.mp3
Riddle.mp3
Riders.mp3
Riot.mp3
Rip & Tear.mp3
Riptide.mp3
RISE - Remix.mp3
Rise Up.mp3
Rising Tide.mp3
Royalty.mp3
Rumble.mp3
Run (1).mp3
Run It.mp3
Run.mp3
Running Away.mp3
Running Up That Hill (A Deal With God).mp3
SAD!.mp3
Sag My Pants.mp3
Sahara.mp3
SAOKO.mp3
Saturn.mp3
Say Yeah.mp3
Sayrena Ya Donia.mp3
Scared of the Dark (feat. XXXTENTACION).mp3
Scary Garry.mp3
Se Acabo (feat. Method Man).mp3
Secret - does not apply.mp3
See You Again (feat. Charlie Puth).mp3
Set Fire to the Rain.mp3
Seven Nation Army.mp3
Shady.mp3
Shake That.mp3
Shamandora.mp3
She Bad.mp3
She Cheated Again.mp3
She's Got a Gun.mp3
She.mp3
Shook Ones, Pt. II.mp3
Sick of U (with Oliver Tree).mp3
SICKO MODE.mp3
Sign.mp3
Sing About Me, I'm Dying Of Thirst.mp3
Sinners (feat. Thomas LaRosa).mp3
Sirens Over Paris.mp3
Six Speed.mp3
Skitzo.mp3
Skyfall - Slowed + Reverb.mp3
Skyfall.mp3
Slap!.mp3
SLAUGHTER HOUSE.mp3
Smack That.mp3
Smart Cube.mp3
Smells Blood.mp3
SMOKE (feat. Jasiah).mp3
Snooze.mp3
Snow in Summer.mp3
Snowman.mp3
So High.mp3
Softcore.mp3
Somebody That I Used To Know.mp3
Someone Like You.mp3
Somnus.mp3
Song of the Ancients _ Devola.mp3
Sorrowful Stone (Soundtrack from the Anime _Fullmetal Alchemist_ Brotherhood).mp3
Souvenir.mp3
Space Cadet (feat. Gunna).mp3
Speedom (Wwc2).mp3
Spinnin.mp3
SPIT IN MY FACE!.mp3
squabble up.mp3
Sriracha.mp3
Stainless.mp3
Stan - Instrumental.mp3
Standby.mp3
Starbound.mp3
Stardust Crusaders.mp3
Stayin' Alive.mp3
Step Back!.mp3
Stick Up.mp3
Still D.R.E..mp3
Still Hot.mp3
Stomp.mp3
Stories of Hope.mp3
Stranger Things.mp3
Strangers.mp3
Street Fight.mp3
Stronger (1).mp3
Stronger.mp3
STUCK IN A DAZE.mp3
Stuffin.mp3
Stunna.mp3
Stupid.mp3
Suicide Squad (feat. Jarren Benton & Locksmith).mp3
Summer Walk.mp3
Sunflower - Spider-Man_ Into the Spider-Verse.mp3
SUNRISE (Slowed + Reverb).mp3
Superhero (Heroes & Villains) [with Future & Chris Brown].mp3
Superlife.mp3
Surface.mp3
Surround Sound (feat. 21 Savage & Baby Tate).mp3
Survival of the Fittest.mp3
Survivor.mp3
Switch Lanes.mp3
Take Over.mp3
Talk (feat. Tech N9ne & Devvon Terrell).mp3
Talk Dat Shit To Me.mp3
Talk talk featuring troye sivan.mp3
Talking Body - KREAM Remix.mp3
Taste (feat. Offset).mp3
Taste.mp3
Telepatiax (Slowed) - Remix.mp3
telepatía.mp3
Tell Me.mp3
Terrorwave.mp3
Test & Recognise - Flume Re-work.mp3
test (2).py
test.py
Thanks Officer.mp3
The Adventures of Moon Man & Slim Shady (with Eminem).mp3
The Alchemist.mp3
THE BADDEST.mp3
The Ballad of G and X __ Interlude.mp3
The City.mp3
The Color of Depression.mp3
The Delicious Last Course.mp3
The Edge.mp3
The FPS Rap Battle.mp3
The Good Part.mp3
The Hanging Tree.mp3
The Hills X Creepin X The Color Violet.mp3
The Illest.mp3
The Last of Us.mp3
The Motto.mp3
The Next Episode.mp3
The One.mp3
The Only Thing They Fear Is You.mp3
The Perfect Girl - Arabic Version.mp3
The Real Slim Shady.mp3
The Ringer.mp3
The Search.mp3
The Way (Instrumental).mp3
Thelema.mp3
These Days.mp3
Think.mp3
this girl.mp3
Those Kinda Nights (feat. Ed Sheeran).mp3
Thrillin.mp3
Through and Through.mp3
Tick Tick Boom (feat. BygTwo3).mp3
TiK ToK.mp3
TIL FURTHER NOTICE (feat. James Blake & 21 Savage).mp3
Till It's Done.mp3
Time of my Life.mp3
Time Warp.mp3
Titanfall 2_ My Pills.mp3
Toca Toca.mp3
Tongue - super slowed.mp3
Tongue.mp3
Top Of The World.mp3
Traitor's Requiem.mp3
Trendsetter.mp3
Trisha's Lullaby (Soundtrack from the Anime _Fullmetal Alchemist_ Brotherhood).mp3
Turn It Up.mp3
Turn off the Lights (feat. Alexis Roberts).mp3
Tuyo (Narcos Theme) [Extended Version] - A Netflix Original Series Soundtrack.mp3
tv off (feat. lefty gunplay).mp3
Twilight.mp3
Twirlanta - Slowed Down Version.mp3
Twisted.mp3
Uebok Gotta Run.mp3
Ultimately.mp3
Ultimatum.mp3
Ultralight Beam.mp3
Unaccommodating (feat. Young M.A).mp3
Unforgettable - The Four Performance.mp3
Unity.mp3
UNIVERSAL COLLAPSE.mp3
Unstoppable.mp3
Until We Die.mp3
Up Down (Step & Walk).mp3
Update.mp3
UR FINAL MESSAGE - Slowed + Reverb.mp3
Ur Final Message - Slowed.mp3
Uragirimonono Requiem - English Ver..mp3
Uragirimonono Requiem - Giorno Ver..mp3
Vault.mp3
vendetta!.mp3
Venom.mp3
Venus.mp3
Vertigo.mp3
VILLAIN.mp3
Violence.mp3
Violet.mp3
Vitality.mp3
Voice of no Return.mp3
Von dutch.mp3
Wack Ass Rappers.mp3
Waiting.mp3
Wake Up (feat. Jessi Mason).mp3
WAKE UP!.mp3
Walk It Talk It.mp3
Wana.mp3
WARDOGZ.mp3
WARNING.mp3
Warriors.mp3
Watch It Burn.mp3
Watch The Party Die.mp3
Water Fountain.mp3
Weakest Link.mp3
Weeble Wobble.mp3
Weight of the World - English Version - J'Nique Nicole.mp3
Weight of the World the End of YoRHa.mp3
Wellerman - Sea Shanty.mp3
Werk.mp3
West Coast Love.mp3
What A Wonderful World.mp3
What They Want_.mp3
What's Up Danger (with Black Caviar).mp3
whatdoyoudo_.mp3
When I Was Young.mp3
When the Credits Roll.mp3
Which Direction_.mp3
Wicked.mp3
Wings.mp3
Wish You'd Make Me Cry.mp3
Witch Doctor.mp3
Without Me.mp3
Without You (feat. Victoria Zaro).mp3
Work.mp3
World's Smallest Violin.mp3
Worldwide Choppers (feat. Ceza, JL B.Hood, Uso, Yelawolf, Twista, Busta Rhymes, D-Loc and Twisted Insane).mp3
WORTH NOTHING - Fast & Furious_ Drift Tape_Phonk Vol 1.mp3
Wrath (1).mp3
WRATH.mp3
Writing's On The Wall - From _Spectre_ Soundtrack.mp3
Wtf U Mean (feat. Freddie Dredd).mp3
WTF!.mp3
Wu Tang Forever (ft. Ghostface Killah, Raekwon, RZA, Method Man, Inspectah Deck, Cappadonna, Jackpot Scotty Wotty, U-God, Masta Killa, GZA).mp3
XO Tour Llif3.mp3
Xxxxxxx.mp3
Yalmidan.mp3
Yonkers.mp3
Yoshikage Kira Theme.mp3
you & i.mp3
You & Jennifer.mp3
You & Me - Flume Remix.mp3
You Don't Know Me (In the Style of Jax Jones (feat. Raye)).mp3
You Gon’ Learn (feat. Royce Da 5'9_ & White Gold).mp3
You Got Jokes.mp3
You Know How We Do It.mp3
Young & Alive - Bazzi vs. Haywyre Remix.mp3
Young Jesus.mp3
Your Eyes.mp3
YOUR FINAL MESSAGE.mp3
YouTube Cypher, Vol. 2.mp3
Zenith.mp3
_names.py
_rename.py
¿ (feat. Halsey).mp3
ÁGUA DE BEBER.mp3
Øfdream_ Thelema (Slowed & Bass Boosted).mp3
Мой мармеладный (Я не права).mp3
Отключаю телефон (Slowed).mp3
باظت.mp3
بنت متناكة.mp3
مش حقيقة.mp3
ولعانه.mp3
ターゲット サスペンス C.mp3
ブルーバード.mp3
交錯.mp3
名探偵コナン メイン・テーマ - 世紀末ヴァージョン.mp3
名探偵コナン メイン・テーマ - 暗殺者ヴァージョン.mp3
名探偵コナン メイン・テ－マ - 標的ヴァージョン.mp3
因果.mp3
対決のテーマ - 摩天楼ヴァージョン.mp3
最恐.mp3
爆破犯人のテーマ.mp3
記憶喪失 (影).mp3
陰謀 - 摩天楼ヴァージョン.mp3
青のすみか.mp3
}
    """
def remove_think_tags(text: str) -> str:
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    cleaned_text = cleaned_text.strip()
    return cleaned_text

for chunk in ollama.generate(model=model,prompt=prompt,stream=True):
    print(chunk["response"],end="",flush=True)