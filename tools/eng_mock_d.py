# 학평형 영어 지문 3 (자체 제작) — 표기법은 eng_mock_a.py와 같음
D = [
dict(p="""Most people believe that a good memory means remembering as much as possible. However, forgetting plays an important role in how the brain works. If we remembered every detail of every day, our minds would be [flooded|emptied] with useless information, and it would be hard to find what really matters. By letting go of unimportant details, the brain makes room for {general|generally|명사 patterns 수식 → 형용사} patterns and useful knowledge. For example, you do not need to remember every time you crossed a street; you only need the rule of looking both ways. Forgetting, then, is not simply a failure of memory but <a process that helps us think more clearly>.""",
m=[('요지', ['망각은 불필요한 정보를 덜어 내어 사고를 돕는 역할을 한다.', '좋은 기억력은 모든 것을 기억하는 능력이다.', '망각은 뇌 기능이 손상되었다는 신호이다.', '길을 건널 때마다 상황을 기억해야 한다.', '기억력 훈련으로 망각을 완전히 막을 수 있다.']),
   ('제목', ['The Useful Side of Forgetting', 'How to Remember Everything', 'Forgetting: A Sign of Illness', 'Rules for Crossing the Street', 'Memory Champions of the World'])],
b=['a weakness that must be fixed', 'a sign of growing old', 'an error caused by stress', 'a habit we should avoid'],
s=("Forgetting ___(A)___ unimportant details, which allows the brain to focus on ___(B)___ knowledge.", [('removes', 'useful'), ('stores', 'useful'), ('removes', 'random'), ('creates', 'detailed'), ('hides', 'false')]),
x='망각은 불필요한 세부 사항을 지워 일반적 패턴과 유용한 지식에 집중하게 한다.'),

dict(p="""Wolves were once removed from Yellowstone National Park, and for nearly seventy years, the park had no wolves at all. During this time, the number of elk grew rapidly. The elk ate young trees along the rivers, and the riverbanks began to [erode|recover]. When wolves were reintroduced in 1995, something remarkable happened. The elk began to avoid open valleys {where|which|장소 + 완전한 절 → where} they could easily be hunted. Trees grew back, birds returned, and beavers built new dams. Even the shape of some rivers changed. This chain of effects shows that a single predator can <influence an entire ecosystem>.""",
m=[('주제', ['the wide effects of reintroducing wolves to Yellowstone', 'reasons elk prefer open valleys', 'how beavers build dams', 'the history of national parks', 'methods of hunting wolves']),
   ('제목', ['How Wolves Changed the Rivers', 'Why Elk Are Dangerous', 'Yellowstone Without Animals', 'The Best Way to Hunt Elk', 'Beavers: Enemies of Trees'])],
b=['disappear without any effect', 'be replaced by other animals easily', 'harm only the animals it eats'],
i=('a single predator', ['one hunting species at the top of the food chain', 'a lonely wolf without a pack', 'one hunter in the park', 'a dangerous visitor', 'a type of tree']),
r="Yellowstone was established as the first national park in the United States in 1872.",
x='늑대의 재도입이 엘크의 행동을 바꾸고 생태계 전체에 연쇄 효과를 일으켰다.'),

dict(p="""When a new product fails, companies often blame the design or the price. But sometimes the real problem is timing. A video-calling device introduced decades ago, for example, was technically impressive but [failed|succeeded] because few people had the fast internet connections needed to use it. Years later, similar technology became a huge success once networks had improved. An idea {that|what|선행사 idea → that} arrives too early may be ignored, while one that arrives too late faces strong competition. Successful innovators therefore pay close attention not only to {what|that|선행사 없음 → what} they create but also to <whether the world is ready for it>.""",
m=[('요지', ['혁신이 성공하려면 아이디어만큼 시기가 중요하다.', '제품 실패의 원인은 항상 디자인이다.', '새로운 기술은 빨리 출시할수록 좋다.', '가격을 낮추면 모든 제품이 성공한다.', '경쟁이 심한 시장은 피해야 한다.']),
   ('제목', ['Timing: The Hidden Key to Innovation', 'Why Cheap Products Always Win', 'The History of Video Calls', 'Design Matters Most', 'Never Launch a New Product'])],
b=['how much it costs to produce', 'who designed the product', 'what color it should be'],
s=("The ___(A)___ of a product's release can decide its success as much as its ___(B)___.", [('timing', 'quality'), ('price', 'quality'), ('timing', 'name'), ('place', 'color'), ('size', 'speed')]),
x='제품의 성공은 아이디어뿐 아니라 세상이 준비되었는지, 즉 시기에 달려 있다.'),

dict(p="""Many people try to motivate themselves by imagining success. They picture themselves crossing the finish line or receiving an award. Surprisingly, research suggests that positive fantasies alone can [reduce|boost] the energy we put into reaching our goals. When we imagine success vividly, the brain partly experiences it as if it {has|had|as if 가정법 과거 → had} already happened, so we feel less need to act. A more effective method combines dreaming with planning. After picturing the goal, we should identify the obstacles {standing|stood|능동 → standing} in our way and decide in advance how to deal with them. Dreams give us direction, but <only plans give us a road>.""",
m=[('주장', ['목표를 이루려면 성공을 상상하는 데 그치지 말고 장애물에 대한 계획을 세워야 한다.', '성공한 모습을 자주 상상할수록 목표를 쉽게 이룬다.', '목표는 크게 세울수록 좋다.', '장애물을 생각하면 의욕이 떨어지므로 피해야 한다.', '꿈은 현실과 관계가 없으므로 버려야 한다.']),
   ('요지', ['긍정적 상상만으로는 부족하며 장애물 대비 계획이 함께 필요하다.', '상상 속 성공 경험은 실제 행동을 늘린다.', '목표를 이루는 데 계획은 중요하지 않다.', '시상식 장면을 떠올리면 동기가 커진다.', '꿈을 꾸지 않는 사람이 더 성공한다.'])],
b=['imagination is all we need', 'goals should be kept secret', 'obstacles are best ignored'],
i=('feel less need to act', ['become less motivated to take action', 'need more rest', 'act without thinking', 'feel physically tired', 'stop dreaming completely']),
x='긍정적 상상만으로는 행동 에너지가 줄어들 수 있어 장애물 대비 계획이 필요하다.'),

dict(p="""Every language borrows words from others. English, for instance, took 'piano' from Italian, 'tea' from Chinese, and 'robot' from Czech. Korean has also adopted many foreign words, especially in areas such as technology and fashion. Some people worry that this borrowing {threatens|threaten|주어 borrowing(단수)} the purity of a language. However, history shows that borrowing usually [enriches|weakens] a language rather than destroying it. Borrowed words are adapted to the sounds and grammar of their new home, and they often fill gaps where no suitable word existed. A language that borrows is not losing itself; it is <a living system that grows through contact>.""",
m=[('요지', ['외래어 차용은 언어를 파괴하기보다 풍부하게 만든다.', '외래어는 언어의 순수성을 해친다.', '영어는 다른 언어에서 단어를 빌리지 않는다.', '기술 용어는 반드시 고유어로 바꿔야 한다.', '언어는 접촉 없이 고립될 때 발전한다.']),
   ('주제', ['the positive role of borrowed words in languages', 'the origin of the word "robot"', 'why fashion words are difficult', 'rules for pronouncing Italian', 'the decline of the Czech language'])],
b=['a fixed set of rules that never changes', 'a weak system that will soon disappear', 'a copy of a more powerful language'],
r="Czech is spoken by about ten million people today.",
x='단어 차용은 언어를 풍부하게 하며 언어는 접촉을 통해 성장하는 체계이다.'),

dict(p="""It is tempting to believe that a famous expert is always right. Yet experts can be [mistaken|correct], especially when they speak about topics outside their own field. A brilliant physicist may know little about nutrition, and a successful businessperson may have no special insight into medicine. When we hear a claim, it is wiser to ask {what|which|선행사 없음 → what} evidence supports it than to ask who said it. Good evidence can be checked by others, while a famous name cannot replace data. Respecting experts is reasonable, but we should <judge ideas by their support, not by their source>.""",
m=[('주장', ['주장을 판단할 때는 누가 말했는지보다 근거를 따져야 한다.', '유명한 전문가의 말은 항상 믿어야 한다.', '전문가의 의견은 무시해야 한다.', '영양에 관해서는 물리학자에게 물어야 한다.', '자료보다 명성이 더 중요하다.']),
   ('제목', ['Evidence Before Fame', 'Why Experts Are Always Right', 'Famous People Know Everything', 'How to Become an Expert', 'The Business of Medicine'])],
b=['trust whoever is most famous', 'ignore all scientific data', 'follow the majority opinion'],
x='권위가 아니라 근거로 주장을 판단해야 한다.'),

dict(p="""Elephants are known for their excellent memories, and this ability helps them survive. In times of drought, the oldest female in a herd, called the matriarch, often leads the group to distant water holes she visited decades earlier. Herds {led|leading|herds가 '이끌어지는' 수동 → led} by older matriarchs are more likely to survive severe droughts than those with younger leaders. Older matriarchs are also better at [recognizing|ignoring] the calls of dangerous predators such as lions. For this reason, when poachers kill the oldest elephants for their large tusks, the whole herd loses <a library of survival knowledge>.""",
m=[('주제', ['the importance of older female elephants\' knowledge for herd survival', 'the size of elephant tusks', 'how lions hunt elephants', 'the causes of droughts in Africa', 'why young elephants lead herds'])],
b=['its strongest fighter', 'its youngest member', 'its favorite food'],
i=('a library of survival knowledge', ['the experience needed to find water and avoid danger', 'a building full of books', 'the ability to make loud calls', 'a collection of elephant tusks', 'the strength to fight poachers']),
s=("Older matriarchs' ___(A)___ helps elephant herds survive, so their loss is ___(B)___ to the group.", [('memory', 'harmful'), ('memory', 'helpful'), ('size', 'harmful'), ('speed', 'unimportant'), ('youth', 'beneficial')]),
x='나이 든 암컷 코끼리의 기억과 경험이 무리 생존에 결정적이다.'),

dict(p="""Rain falling on city streets is often treated as a problem to be removed as quickly as possible. It runs off roofs and roads into drains and then into rivers, carrying oil and trash with it. Some cities are now taking a different approach. They are building 'rain gardens,' shallow areas planted with grasses and shrubs {that|what|선행사 areas → that} collect rainwater and let it soak slowly into the ground. These gardens [filter|add] pollutants, reduce flooding, and provide homes for insects and birds. By working with nature rather than against it, cities can turn rainwater from <a burden into a resource>.""",
m=[('제목', ['Rain Gardens: Turning a Problem into a Benefit', 'Why Cities Need Bigger Drains', 'The Danger of Planting Shrubs', 'How to Keep Streets Dry Forever', 'Rain Is the Enemy of Cities']),
   ('요지', ['빗물 정원은 빗물을 오염원이 아닌 자원으로 바꾼다.', '빗물은 최대한 빨리 하수구로 흘려보내야 한다.', '빗물 정원은 홍수를 늘린다.', '도시에는 식물을 심지 말아야 한다.', '빗물은 오염 물질을 운반하지 않는다.'])],
b=['a resource into a burden', 'a river into a road', 'a garden into a parking lot'],
r="Many people enjoy the sound of rain while they sleep.",
x='빗물 정원은 빗물을 흡수·정화하여 부담이던 빗물을 자원으로 바꾼다.'),

dict(p="""When people receive a gift, they usually value it more if it was chosen with care. However, research shows that givers and receivers think differently about gifts. Givers often try to surprise the receiver with something unexpected, while receivers tend to prefer gifts they actually asked for. In one study, people who received an item from their own wish list felt more [appreciative|disappointed] than those who received a 'thoughtful' surprise. Givers worry that a requested gift seems {impersonal|impersonally|seem의 보어 → 형용사}, but receivers see it as a sign that the giver listened. Sometimes the most thoughtful gift is <simply the one that was asked for>.""",
m=[('요지', ['선물을 받는 사람은 깜짝 선물보다 자신이 원했던 선물을 더 좋아한다.', '깜짝 선물이 가장 정성 어린 선물이다.', '선물을 주는 사람과 받는 사람의 생각은 같다.', '요청받은 선물은 성의가 없어 보인다.', '비싼 선물일수록 만족도가 높다.']),
   ('제목', ['Give What They Asked For', 'The Joy of Surprise Gifts', 'Why Gifts Should Be Expensive', 'How to Wrap a Present', 'Never Use a Wish List'])],
b=['the most expensive one', 'the most surprising one', 'one made by hand'],
s=("Givers prefer ___(A)___ gifts, but receivers are more pleased with gifts they ___(B)___.", [('surprising', 'requested'), ('surprising', 'avoided'), ('expensive', 'requested'), ('requested', 'disliked'), ('practical', 'forgot')]),
x='받는 사람은 깜짝 선물보다 자신이 요청한 선물을 더 고맙게 여긴다.'),

dict(p="""Night skies around the world are getting brighter. Streetlights, signs, and buildings send so much light into the sky that many people can no longer see the Milky Way. This light pollution affects more than our view of the stars. Many birds that migrate at night use the stars to navigate, and bright city lights can draw them off course, sometimes {causing|caused|분사구문 → causing} them to crash into buildings. Sea turtle hatchings, which find the ocean by moving toward the brightest horizon, may head inland instead. The good news is that light pollution is easy to [reduce|increase]. Shielding lights so they point downward and turning off unnecessary lights can <bring back the darkness that nature needs>.""",
m=[('주제', ['the effects of light pollution and ways to reduce it', 'how stars guide ships', 'the beauty of the Milky Way', 'the history of streetlights', 'why sea turtles avoid the ocean']),
   ('주장', ['자연을 위해 불필요한 조명을 줄여 빛 공해를 막아야 한다.', '도시는 밤에 더 밝게 조명해야 안전하다.', '철새 보호를 위해 건물을 높게 지어야 한다.', '바다거북을 내륙으로 옮겨야 한다.', '별을 보려면 시골로 이사해야 한다.'])],
b=['make cities look more beautiful at night', 'help birds fly faster', 'save more money for cities'],
i=('draw them off course', ['lead them away from their correct route', 'make them draw pictures', 'help them find food', 'teach them new songs', 'make them fly higher']),
x='빛 공해는 동물에게 해를 끼치므로 조명을 가리거나 끄는 방식으로 줄여야 한다.'),
]

LETTERS2 = [
("""Dear Ms. Johnson,
I am a member of the Pinewood High School Environmental Club. Next month, we are planning a beach clean-up event at Sandy Point, and we expect about fifty students to participate. We would like to ask whether your company could donate gloves, trash bags, and drinking water for the volunteers. Your support would help us protect our beautiful coastline. If you are able to help, please contact me at the email address below.
Thank you,
Brian Cho""", ['해변 정화 활동에 필요한 물품 후원을 요청하려고', '해변 정화 활동 일정 변경을 알리려고', '환경 동아리 신입 회원을 모집하려고', '회사의 환경 보호 활동에 감사하려고', '해변 출입 금지 구역을 안내하려고']),
("""Dear Library Users,
We are pleased to announce that the Central Library will begin a new e-book lending service starting March 1. Library members will be able to borrow up to five e-books at a time and read them on their phones, tablets, or computers. To use the service, simply log in to our website with your library card number. A short guide is available at the information desk for anyone who needs help getting started.
Sincerely,
Central Library""", ['전자책 대출 서비스의 시작을 안내하려고', '도서관 회원 가입을 권유하려고', '도서관 휴관 일정을 공지하려고', '도서 반납 기한 준수를 요청하려고', '새 컴퓨터 구입 계획을 알리려고']),
("""Dear Professor Kim,
I attended your lecture on ocean science at the city museum last Saturday. Your explanation of how deep-sea creatures produce their own light was fascinating, and it made me decide to study marine biology in the future. I especially enjoyed the videos you showed at the end. I just wanted to let you know how much your lecture meant to me. Thank you for sharing your passion with us.
Best wishes,
Jiwoo Lee""", ['강연에 대한 감사와 감동을 전하려고', '해양 과학 강연을 요청하려고', '박물관 견학 일정을 문의하려고', '강연 영상 자료를 요청하려고', '해양 생물학 진학 상담을 신청하려고']),
("""To Whom It May Concern,
I am writing to report a problem with the bus stop on Cedar Street. The shelter's roof was damaged during last week's storm, and now rain falls directly on people waiting for the bus. Many elderly passengers use this stop every day, and they have nowhere to stay dry. I hope the city can repair the shelter before the rainy season begins. Thank you for your attention.
Sincerely,
Laura Kim""", ['파손된 버스 정류장 지붕의 수리를 요청하려고', '버스 노선 변경을 제안하려고', '버스 운행 시간 연장을 요구하려고', '정류장 신설을 반대하려고', '폭풍 피해 보상을 신청하려고']),
("""Dear Members,
The annual meeting of the Westfield Hiking Club will be held on January 15 at 7 p.m. in the community center. At this meeting, we will review last year's activities and elect new club officers. We will also discuss next year's hiking schedule, so please bring your ideas for new trails. Light refreshments will be served. We hope to see all of you there.
Best regards,
The Westfield Hiking Club Committee""", ['동호회 연례 회의 개최를 알리고 참석을 독려하려고', '새 등산로 개장을 홍보하려고', '동호회 회비 인상을 공지하려고', '등산 안전 수칙을 안내하려고', '동호회 해산을 통보하려고']),
]

NARR2 = [
("""Ben had prepared his speech for the student council election for weeks. When his name was called, he walked onto the stage and looked at the crowd. Hundreds of faces stared back at him. His mouth felt dry, and the paper in his hand trembled. But as he began to speak, he noticed his friends in the front row nodding and smiling. His voice grew steadier, and by the end, the whole auditorium was clapping.""", 'nervous → confident', ['excited → bored', 'calm → annoyed', 'proud → regretful', 'happy → lonely'], 'Ben'),
("""Grace opened the box from her grandfather, who lived far away. Inside was an old wooden music box that she had loved as a little girl. A small note said, "I fixed it for you." When she turned the key, the familiar melody filled the room. Tears came to her eyes as she remembered the summers she had spent at his house.""", 'touched and grateful', ['annoyed and impatient', 'frightened and nervous', 'bored and indifferent', 'jealous and bitter'], 'Grace'),
("""Daniel had been told that the final exam would cover only chapters one to five. He studied those chapters carefully. But when he turned over the test paper, he saw questions from chapters six and seven, which he had not even opened. He looked around the room in panic. Everyone else seemed to be writing calmly.""", 'confident → panicked', ['nervous → relieved', 'bored → excited', 'angry → calm', 'sad → hopeful'], 'Daniel'),
("""Zoe's tomato plants had been struggling all summer. The leaves were yellow, and not a single tomato had appeared. She was about to give up. One morning, however, she went out to water them and saw something red among the leaves. Bending closer, she found three ripe tomatoes hanging from a stem. She laughed out loud and ran inside to tell her mother.""", 'discouraged → delighted', ['excited → disappointed', 'calm → frightened', 'pleased → annoyed', 'curious → bored'], 'Zoe'),
("""The museum was quiet as Aiden walked through the dinosaur hall. Huge skeletons towered above him, and he stopped in front of a Tyrannosaurus, staring at its enormous teeth. He read every sign, asked the guide a dozen questions, and took notes in his notebook. When his parents said it was time to leave, he begged for just ten more minutes.""", 'curious and fascinated', ['bored and sleepy', 'scared and upset', 'angry and irritated', 'lonely and sad'], 'Aiden'),
]
