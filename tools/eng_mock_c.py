# 학평형 영어 18·19·26·27·28번 유형 지문 (자체 제작, 등장 인물·단체는 모두 가상)
# LETTERS: (편지, [목적 정답, 오답4])  — 18번 '글의 목적'
LETTERS = [
("""Dear Ms. Carter,
I am writing on behalf of the Riverside High School Science Club. Each spring, our members hold a science fair for elementary school children in our town. This year, we hope to include a session on renewable energy, and we know that you have given many popular talks on this topic. We would be truly honored if you could join us on May 14 and speak to the children for about thirty minutes. Your talk would inspire many young minds. Please let us know whether your schedule allows it.
Sincerely,
Daniel Park""", ['과학 박람회에서 강연해 줄 것을 요청하려고', '과학 박람회 일정 변경을 알리려고', '재생 에너지 동아리 가입을 권유하려고', '강연에 대한 감사 인사를 전하려고', '초등학생 대상 과학 캠프를 홍보하려고']),
("""To the Manager,
Last Saturday, I ordered a birthday cake from your bakery for my daughter's party. When I opened the box at home, I found that the cake had a different design from the one I had chosen, and the name on top was spelled incorrectly. My daughter was very disappointed. I have always enjoyed your products, so this was surprising. I would appreciate it if you could refund the cost of the cake or offer a replacement for a future order. I have attached a photo of the cake and my receipt.
Regards,
Helen Moore""", ['주문한 케이크의 문제에 대해 보상을 요구하려고', '생일 파티에 제빵사를 초대하려고', '새로운 케이크 디자인을 제안하려고', '케이크 주문 날짜를 변경하려고', '빵집의 친절한 서비스에 감사하려고']),
("""Dear Residents,
As many of you know, the elevator in Building C has been out of order since Monday. We sincerely apologize for the inconvenience this has caused, especially to elderly residents and families with small children. The replacement parts have finally arrived, and repair work will take place this Thursday from 9 a.m. to 5 p.m. During this time, the stairs will remain open. If you need help carrying heavy items, please contact the management office, and our staff will be glad to assist you.
Best regards,
Green Hill Apartments Management Office""", ['엘리베이터 수리 일정과 지원 방법을 안내하려고', '새 엘리베이터 설치 비용을 공지하려고', '계단 청소 일정을 알리려고', '관리 사무소 직원 채용을 공고하려고', '주민 회의 참석을 요청하려고']),
("""Dear Mr. Lewis,
Thank you for your interest in volunteering at the Maple Community Library. We received many applications this year, and we were impressed by your experience in teaching reading to children. Unfortunately, all of our weekend positions have already been filled. However, we still need volunteers on Wednesday afternoons to help with our homework club. If this time works for you, please reply by Friday so that we can arrange a short orientation.
Warm regards,
Sarah Kim, Volunteer Coordinator""", ['다른 시간대의 자원봉사 자리를 제안하려고', '자원봉사 지원서 제출을 독촉하려고', '도서관 개관 시간 변경을 알리려고', '숙제 동아리 운영을 중단하려고', '독서 교육 강사를 채용하려고']),
("""Dear Parents,
Our school has noticed that many students arrive late because of heavy traffic near the main gate in the morning. To improve safety and reduce congestion, we ask that parents who drive their children to school use the drop-off area on Elm Street instead of stopping in front of the main gate. Teachers will be stationed there from 7:50 to 8:20 a.m. to guide students. We appreciate your cooperation in keeping our students safe.
Sincerely,
Principal Robert Hayes""", ['학생 하차 장소 변경에 협조를 요청하려고', '등교 시간 변경을 알리려고', '학교 정문 공사 일정을 안내하려고', '교사 회의 개최를 공지하려고', '통학 버스 운행 중단을 알리려고']),
("""Dear Editor,
I read with great interest your recent article about the closing of the public swimming pool on Oak Avenue. As a lifelong resident, I learned to swim there, and so did my children. The article stated that the city has no funds for repairs. However, many residents would be willing to help. I propose that the city organize a fundraising event, and I am ready to volunteer my time to make it happen. I hope your newspaper can help spread the word.
Sincerely,
Mark Rivera""", ['수영장 보수를 위한 모금 행사를 제안하려고', '신문 기사 내용의 오류를 지적하려고', '수영 강습 등록 방법을 문의하려고', '수영장 폐쇄 결정에 감사하려고', '새로운 수영장 건설을 반대하려고']),
("""Hello Members,
Thank you all for making our winter book drive such a success. Together, we collected more than 2,000 books, which were delivered to three rural schools last week. The teachers there sent us photos of their students reading the new books, and their smiles say it all. None of this would have been possible without your generosity and hard work. We look forward to working with you again on future projects.
With gratitude,
Lily Chen, Club President""", ['도서 기부 행사 참여에 감사하려고', '새로운 도서 기부 행사를 홍보하려고', '시골 학교의 도서관 개관을 알리려고', '동아리 회장 선거를 공지하려고', '기부 도서 목록을 요청하려고']),
("""Dear Customer Service,
I purchased a pair of wireless earphones from your online store two weeks ago. Since yesterday, the left earphone has stopped producing any sound, even though it is fully charged. I have tried resetting the device as described in the manual, but the problem continues. As the product is still under warranty, I would like to know how I can send it in for repair or exchange. My order number is 45-2219.
Thank you,
Jason Lee""", ['고장 난 제품의 수리나 교환 방법을 문의하려고', '이어폰의 새로운 기능을 제안하려고', '주문한 제품의 배송 지연에 항의하려고', '제품 설명서의 오류를 지적하려고', '보증 기간 연장을 요청하려고']),
("""Dear Coach Thompson,
My name is Emma Wilson, and I am a first-year student at Lakeview High School. I have played basketball since elementary school, and I would love to join the school team. Unfortunately, I was sick with the flu during the tryouts last week and could not attend. I understand that the team has already been selected, but I wonder if there might be a chance for me to try out separately. I would be grateful for any opportunity to show my skills.
Sincerely,
Emma Wilson""", ['농구팀 입단 테스트를 따로 받을 수 있는지 문의하려고', '농구팀 훈련 일정 변경을 요청하려고', '입단 테스트 결과에 이의를 제기하려고', '농구팀 탈퇴 의사를 밝히려고', '새 코치 부임을 축하하려고']),
("""To All Club Members,
Due to the heavy rain forecast for this weekend, the hiking trip to Mount Bell scheduled for Saturday has been postponed. Safety is our top priority, and the mountain trails can be very slippery after rain. The new date is Saturday, October 21, and the meeting time and place will remain the same. If you can no longer attend on the new date, please let me know by Wednesday so that I can update the bus reservation.
Best,
Kevin Brooks, Hiking Club Leader""", ['등산 일정이 연기되었음을 알리려고', '등산로 정비 작업을 요청하려고', '새 회원 모집을 홍보하려고', '버스 예약 비용을 청구하려고', '등산 장비 구입을 권유하려고']),
("""Dear Ms. Anderson,
I am the owner of Sunny Café on Main Street. For the past five years, local artists have displayed their paintings on our walls, and our customers have loved them. Our current exhibition ends this month, and I have heard wonderful things about the artwork your students create. Would your art class be interested in holding an exhibition at our café next month? There would be no fee, and the students could even sell their works if they wish.
Kind regards,
Paul Martin""", ['카페에서 학생 작품 전시회를 열 것을 제안하려고', '카페 개업 소식을 알리려고', '미술 수업 등록을 문의하려고', '그림 구입 가격을 협상하려고', '전시회 일정 취소를 통보하려고']),
("""Dear Neighbors,
I am writing to let you know that our family will be renovating our kitchen from June 3 to June 14. The workers will usually be here between 9 a.m. and 6 p.m. on weekdays, and there may be some noise during this time. We will do our best to keep the street clean and to avoid blocking parking spaces. We apologize in advance for any inconvenience. If you have any concerns, please feel free to knock on our door.
Thank you for your understanding,
The Garcia Family""", ['주방 공사로 인한 불편에 대해 양해를 구하려고', '이웃에게 공사 업체를 추천하려고', '주차 공간 배정을 요청하려고', '이사 소식을 알리려고', '소음 문제에 항의하려고']),
("""Dear Members of the Youth Orchestra,
I am delighted to announce that our orchestra has been invited to perform at the National Youth Music Festival in August. This is a wonderful recognition of the hard work you have all put in this year. To prepare, we will hold extra rehearsals every Tuesday evening starting next week. Please check the attached schedule and make sure that you can attend. I am sure we will make our community proud.
Warmly,
Conductor Maria Lopez""", ['음악 축제 초청 소식과 추가 연습 일정을 알리려고', '오케스트라 단원을 추가 모집하려고', '음악 축제 입장권 구매를 권유하려고', '연습실 사용 규칙을 안내하려고', '지휘자 교체 소식을 전하려고']),
("""Dear Mr. Patel,
Thank you for visiting our animal shelter last weekend and expressing interest in adopting Max, the three-year-old beagle. Before we can complete the adoption, we need to visit your home to make sure it is a safe environment for him. Would any day next week work for you? The visit usually takes about thirty minutes. We look forward to helping Max find his forever home.
Best wishes,
Riverside Animal Shelter""", ['입양 절차를 위한 가정 방문 일정을 정하려고', '보호소 자원봉사 참여를 요청하려고', '입양 신청이 거절되었음을 알리려고', '반려견 훈련 프로그램을 홍보하려고', '보호소 후원금을 요청하려고']),
("""To the Head of the Parks Department,
I am a resident of Westwood, and I often walk my dog in Pine Park. Recently, I have noticed that several streetlights along the main path are not working. Since it gets dark early in winter, the path has become unsafe for walkers and joggers in the evening. I would like to request that these lights be repaired as soon as possible. Thank you for your attention to this matter.
Sincerely,
Grace Hall""", ['공원 가로등 수리를 요청하려고', '공원 산책로 확장을 제안하려고', '반려견 출입 금지에 항의하려고', '공원 개장 시간을 문의하려고', '야간 조깅 모임을 홍보하려고']),
]

# NARR: (이야기, 심경 정답, 오답4, 인물 지칭)
NARR = [
("""It was the final round of the school spelling contest, and only Mia and one other student remained. The judge read out the word, and Mia's mind went completely blank. Her hands were shaking, and she could hear her heart pounding. She closed her eyes and slowly sounded out each syllable. Then she spelled the word letter by letter. There was a pause. "Correct!" said the judge. The audience burst into applause. Mia let out a long breath, and a wide smile spread across her face.""", 'nervous → relieved', ['bored → excited', 'proud → ashamed', 'calm → frightened', 'jealous → grateful'], 'Mia'),
("""Jake had been looking forward to the camping trip for weeks. He packed his bag the night before and could hardly sleep. But in the morning, as he was about to leave, his father received a phone call. The campsite had been closed because of a forest fire nearby. Jake sat down on the steps and stared at his backpack. All his plans had disappeared in a moment.""", 'excited → disappointed', ['bored → curious', 'nervous → confident', 'angry → relieved', 'lonely → delighted'], 'Jake'),
("""Sophie walked into the new school alone. Everyone seemed to know each other, laughing in small groups, and no one looked at her. She sat at the back of the classroom, wishing she could disappear. At lunchtime, a girl with curly hair came over with her tray. "Is this seat taken? I'm Ava. You're new, right? Do you want to join our art club?" Sophie smiled for the first time that day. Maybe this place would not be so bad after all.""", 'lonely → hopeful', ['excited → bored', 'confident → nervous', 'grateful → angry', 'calm → scared'], 'Sophie'),
("""The storm grew stronger as Ethan drove along the dark mountain road. Rain hit the windshield so hard that he could barely see. Suddenly, the headlights went out. He pulled over and sat in complete darkness, listening to the wind howl. His phone showed no signal. Every strange sound outside made him jump. He gripped the steering wheel and wondered how long he would be stuck there.""", 'frightened and anxious', ['relaxed and peaceful', 'proud and satisfied', 'bored and indifferent', 'cheerful and excited'], 'Ethan'),
("""For months, Lucas had practiced the piano piece for the competition, but on the day, he made a mistake in the middle and lost his rhythm. He finished the performance with his face burning. Afterward, he sat alone in the hallway, sure that he had ruined everything. Then his teacher walked over and handed him an envelope. Inside was a note from the judges: "Special Prize for Musical Expression." Lucas read it three times before he could believe it.""", 'ashamed → delighted', ['excited → bored', 'calm → upset', 'curious → indifferent', 'proud → jealous'], 'Lucas'),
("""Grandma's house was exactly as Nora remembered it. The old wooden swing still hung from the oak tree, and the kitchen smelled of cinnamon and fresh bread. She ran her fingers along the piano where she had first learned to play, and she could almost hear her grandmother's gentle voice. Nora sat by the window as the afternoon sun poured in, feeling warm memories wash over her.""", 'nostalgic and peaceful', ['irritated and impatient', 'scared and nervous', 'bored and tired', 'envious and bitter'], 'Nora'),
("""Ryan had spent all night finishing his science project, a model volcano that really erupted. He carried it carefully onto the bus. But when the bus hit a bump, the model slid off his lap and crashed to the floor. The cone cracked in two. Ryan stared at the pieces in disbelief. The presentation was in one hour.""", 'proud → upset', ['anxious → relieved', 'bored → amused', 'upset → grateful', 'calm → indifferent'], 'Ryan'),
("""Hana stood at the edge of the diving board, ten meters above the water. Her legs felt like jelly, and the pool below looked impossibly small. She almost turned back. Then she remembered the months of training with her coach. She took a deep breath, raised her arms, and jumped. When she rose to the surface, she heard her teammates cheering. "I did it!" she shouted, laughing and slapping the water.""", 'scared → thrilled', ['bored → nervous', 'joyful → sad', 'confident → embarrassed', 'relaxed → angry'], 'Hana'),
("""Every day after school, Owen waited by the mailbox for the letter from the university's summer program. Weeks passed, and nothing came. He began to think he had not been accepted. One rainy afternoon, he opened the mailbox without much hope, and there it was: a thick white envelope with the university's logo. His hands trembled as he tore it open and read the first word: "Congratulations." He let out a shout of joy.""", 'hopeless → overjoyed', ['excited → disappointed', 'angry → calm', 'curious → bored', 'pleased → ashamed'], 'Owen'),
("""Chloe had promised to look after her neighbor's cat while he was away. On the third day, she opened the door and the cat dashed outside. She searched the whole street, calling its name, but it was nowhere to be seen. As the sun began to set, she sat down on the doorstep, imagining how she would explain it. Then she heard a soft meow behind her. The cat was sitting on the windowsill, licking its paw as if nothing had happened.""", 'worried → relieved', ['pleased → annoyed', 'bored → curious', 'calm → jealous', 'excited → disappointed'], 'Chloe'),
("""Liam opened his test paper and quickly looked through the questions. To his surprise, every problem was one he had practiced the night before. He picked up his pencil and began to write without hesitation. The answers came to him easily, one after another. By the time the bell rang, he had already checked his work twice.""", 'confident and satisfied', ['nervous and confused', 'bored and sleepy', 'angry and annoyed', 'sorrowful and lonely'], 'Liam'),
("""When Isabel arrived at the theater, she realized she had left the tickets at home. The show was starting in ten minutes, and her home was forty minutes away. Her friends looked at her with wide eyes. Isabel's face turned red as she searched every pocket of her bag again and again. Then the box office manager smiled and said, "Don't worry. We can check your booking with your phone number." Isabel thanked him over and over.""", 'embarrassed → grateful', ['proud → nervous', 'bored → excited', 'calm → jealous', 'grateful → angry'], 'Isabel'),
("""Noah had waited three years to see his best friend, who had moved abroad. At the airport, he checked the arrival board every few minutes. Finally, the doors opened, and he spotted a familiar face in the crowd. Noah ran forward and threw his arms around him. They both started laughing and talking at the same time, as if they had never been apart.""", 'impatient → joyful', ['relaxed → nervous', 'bored → indifferent', 'joyful → sorrowful', 'angry → regretful'], 'Noah'),
("""Ella's team had lost every game that season. In the last match, with seconds left on the clock and the score tied, the ball came to her. She dribbled past two defenders and shot. The ball hit the rim, bounced once, and dropped through the net. The buzzer sounded. Her teammates rushed toward her, screaming. Ella stood frozen for a moment, then jumped into their arms.""", 'tense → triumphant', ['bored → irritated', 'pleased → disappointed', 'calm → regretful', 'confident → frightened'], 'Ella'),
("""Mason had saved his allowance for months to buy a new bicycle. When he finally rode it to school, he locked it carefully in front of the library. After class, he came back to find only the lock lying on the ground. He looked up and down the street, hoping he had made a mistake. His bike was gone.""", 'pleased → devastated', ['nervous → relieved', 'bored → excited', 'scared → calm', 'curious → amused'], 'Mason'),
]

# BIOS: (지문, 인물/대상, [일치하는 진술 5], [일치하지 않는 진술 2])  — 26번 '내용 불일치'
BIOS = [
("""Clara Brennan was born in 1902 in a small fishing village in Ireland. As a child, she spent hours drawing the boats in the harbor. At the age of sixteen, she moved to Dublin to study painting, supporting herself by working in a bookstore. Her early works, mostly seascapes, received little attention. In 1931, however, a series of portraits of fishermen made her famous across Europe. She later founded an art school for children from poor families, which still operates today. Brennan continued painting until her death in 1979.""", 'Clara Brennan',
 ['아일랜드의 작은 어촌에서 태어났다.', '16세에 그림을 공부하러 더블린으로 이주했다.', '서점에서 일하며 생계를 유지했다.', '어부 초상화 연작으로 유명해졌다.', '가난한 가정의 아이들을 위한 미술 학교를 세웠다.'],
 ['초기의 바다 풍경화로 큰 주목을 받았다.', '미술 학교는 그녀의 사망과 함께 문을 닫았다.']),
("""The Atlas moth is one of the largest insects in the world, with wings that can measure up to 25 centimeters across. It is found in the forests of Southeast Asia. The tips of its wings look like the heads of snakes, which may help to scare away predators. Surprisingly, adult Atlas moths have no mouths and cannot eat. They live for only one to two weeks, relying on energy stored when they were caterpillars. During this short time, their main goal is to find a mate and lay eggs.""", 'Atlas moth',
 ['날개 폭이 최대 25 cm에 이른다.', '동남아시아의 숲에 서식한다.', '날개 끝이 뱀의 머리처럼 보인다.', '성충은 입이 없어 먹지 못한다.', '애벌레 시기에 저장한 에너지에 의존한다.'],
 ['성충은 몇 달 동안 산다.', '날개 무늬로 짝을 유인하기 위해 꽃을 먹는다.']),
("""Samuel Okafor was born in Lagos, Nigeria, in 1965. After studying engineering at university, he worked for several years designing bridges. In 1998, he noticed that many rural villages lacked clean drinking water, so he left his job to develop low-cost water filters. His filters, made from clay and sawdust, were cheap enough for families to buy and easy to produce locally. By 2010, more than a million people were using them. Okafor has received several international awards for his work, but he says his greatest reward is seeing children drink safe water.""", 'Samuel Okafor',
 ['나이지리아 라고스에서 태어났다.', '대학에서 공학을 공부했다.', '교량 설계 일을 몇 년간 했다.', '점토와 톱밥으로 만든 정수 필터를 개발했다.', '여러 국제적인 상을 받았다.'],
 ['그의 필터는 비싸서 정부만 구입할 수 있었다.', '2010년까지 필터 사용자는 만 명에 그쳤다.']),
("""The axolotl is a type of salamander native to the lakes around Mexico City. Unlike most amphibians, it keeps its juvenile features throughout its life, including feathery gills on the sides of its head, and it spends its entire life in water. The axolotl is famous for its ability to regrow lost body parts, including legs, parts of its heart, and even parts of its brain. Sadly, it is critically endangered in the wild because of pollution and the loss of its habitat. However, it is widely kept in laboratories and as a pet.""", 'axolotl',
 ['멕시코시티 주변의 호수가 원산지이다.', '평생 어린 시절의 특징을 유지한다.', '머리 양옆에 깃털 모양의 아가미가 있다.', '잃어버린 신체 부위를 다시 자라게 할 수 있다.', '실험실과 애완동물로 널리 길러진다.'],
 ['성체가 되면 육지로 올라와 생활한다.', '야생 개체 수가 매우 많아 보호가 필요 없다.']),
("""Rosa Delgado was a Spanish chef who changed the way people thought about vegetables. Born in Valencia in 1948, she learned to cook from her grandmother, who grew most of the family's food in her garden. Delgado opened her first restaurant in 1975, serving dishes made almost entirely from local vegetables, which was unusual at the time. Critics at first called her menu too simple, but customers loved it. She wrote four cookbooks, and the first was translated into twelve languages. In her later years, she taught cooking to hospital patients.""", 'Rosa Delgado',
 ['발렌시아에서 태어났다.', '할머니에게서 요리를 배웠다.', '1975년에 첫 식당을 열었다.', '네 권의 요리책을 썼다.', '말년에 병원 환자들에게 요리를 가르쳤다.'],
 ['그녀의 식당은 주로 수입 육류 요리를 제공했다.', '첫 요리책은 번역되지 않았다.']),
("""The Great Wall of Gorgan, located in northeastern Iran, is the second-longest defensive wall in the world after the Great Wall of China. Built around the 5th or 6th century, it stretches about 195 kilometers. The wall was made of red bricks, which is why it is sometimes called the 'Red Snake.' More than 30 forts were placed along it, and a canal running beside the wall supplied water for brick making. Although it was once forgotten, archaeologists have studied it intensively since the 2000s.""", 'Great Wall of Gorgan',
 ['이란 북동부에 위치한다.', '세계에서 두 번째로 긴 방어 성벽이다.', "'붉은 뱀'이라고 불리기도 한다.", '성벽을 따라 30개가 넘는 요새가 있었다.', '벽돌 제작에 필요한 물을 운하가 공급했다.'],
 ['돌을 쌓아 만들었다.', '2000년대 이후 연구가 중단되었다.']),
("""Henry Walsh was an American inventor born in Ohio in 1871. He left school at the age of twelve to help on his family's farm, but he spent his evenings reading science books borrowed from the town library. At twenty, he moved to Chicago and worked in a factory that made farm machines. There he invented a new type of plow that required less effort from horses. The invention made him wealthy, and he used much of his money to build public libraries in small towns. More than forty libraries were built with his support.""", 'Henry Walsh',
 ['오하이오에서 태어났다.', '12세에 학교를 그만두었다.', '마을 도서관에서 과학 책을 빌려 읽었다.', '농기계 공장에서 일했다.', '작은 마을에 공공 도서관을 짓는 데 재산을 썼다.'],
 ['대학에서 기계 공학을 전공했다.', '그가 발명한 쟁기는 말의 힘을 더 많이 필요로 했다.']),
("""The emperor penguin is the largest of all penguin species, standing up to 120 centimeters tall. It lives only in Antarctica and breeds during the harsh winter, when temperatures can drop to minus 40 degrees Celsius. After the female lays a single egg, she passes it to the male and returns to the sea to feed. The male keeps the egg warm on his feet for about two months, eating nothing during this time. To survive the cold, males huddle together in large groups, taking turns standing in the warmer center.""", 'emperor penguin',
 ['펭귄 중 가장 큰 종이다.', '남극에서만 산다.', '혹독한 겨울에 번식한다.', '수컷이 약 두 달간 알을 발 위에서 품는다.', '수컷들은 무리 지어 추위를 견딘다.'],
 ['암컷은 한 번에 알을 여러 개 낳는다.', '수컷은 알을 품는 동안 바다에서 먹이를 먹는다.']),
("""Yuki Tanaka is a Japanese architect known for designing buildings that use natural light. Born in Kyoto in 1970, she grew up in a traditional wooden house with paper screens that softened the sunlight. After studying in Tokyo and London, she opened her own studio in 2002. Her most famous work, a public library in Osaka, has a roof made of thousands of small glass panels. In 2019, she won a major international architecture prize. Tanaka also teaches at a university, where she encourages students to design with the environment in mind.""", 'Yuki Tanaka',
 ['교토에서 태어났다.', '전통 목조 가옥에서 자랐다.', '도쿄와 런던에서 공부했다.', '2002년에 자신의 스튜디오를 열었다.', '대학에서 학생들을 가르친다.'],
 ['가장 유명한 작품은 도쿄의 박물관이다.', '2019년에 건축상 수상을 거절했다.']),
("""The Danube is the second-longest river in Europe, flowing about 2,850 kilometers from Germany to the Black Sea. It passes through or along the borders of ten countries, more than any other river in the world. Four capital cities, including Vienna and Budapest, lie on its banks. For centuries, the river served as an important trade route. Today, it is also home to a rich variety of wildlife, especially in the Danube Delta, which is protected as a UNESCO World Heritage Site.""", 'Danube',
 ['유럽에서 두 번째로 긴 강이다.', '독일에서 흑해까지 흐른다.', '세계에서 가장 많은 나라를 지나는 강이다.', '강변에 네 개의 수도가 있다.', '도나우강 삼각주는 유네스코 세계유산으로 보호된다.'],
 ['강변에 위치한 수도는 빈 한 곳뿐이다.', '과거에는 교역로로 거의 쓰이지 않았다.']),
("""Amelia Ross was a British scientist who studied the behavior of crows. Born in 1955, she became fascinated by birds after finding an injured crow in her garden at the age of nine. She studied biology at Cambridge and later spent ten years observing crows in the wild. Her experiments showed that crows can use tools, recognize human faces, and remember people who have treated them badly. Her book on crow intelligence became a bestseller. She retired in 2020 but still gives lectures to young researchers.""", 'Amelia Ross',
 ['1955년에 태어났다.', '9살 때 정원에서 다친 까마귀를 발견했다.', '케임브리지에서 생물학을 공부했다.', '까마귀가 사람의 얼굴을 알아본다는 것을 보여 주었다.', '은퇴 후에도 젊은 연구자들에게 강연한다.'],
 ['까마귀를 실험실에서만 관찰했다.', '그녀의 책은 거의 팔리지 않았다.']),
("""The Sahara Desert covers about nine million square kilometers of North Africa, making it the largest hot desert in the world. Although it is famous for its sand dunes, most of the Sahara is actually covered with rocky plateaus and gravel. Daytime temperatures can exceed 50 degrees Celsius, but nights can be very cold. Scientists have found evidence that the Sahara was once green, with lakes and grasslands, around 6,000 years ago. Today, about two million people live in the desert, many of them in oases.""", 'Sahara Desert',
 ['세계에서 가장 큰 더운 사막이다.', '대부분은 바위 고원과 자갈로 덮여 있다.', '밤에는 매우 추울 수 있다.', '약 6,000년 전에는 호수와 초원이 있었다.', '약 200만 명이 사막에 살고 있다.'],
 ['대부분이 모래 언덕으로 이루어져 있다.', '사람이 전혀 살지 않는다.']),
("""Oliver Grant was a Canadian runner who competed in the 1936 Olympics. Born on a farm in Manitoba, he often ran several kilometers to school each day, which built his endurance. He did not have professional training until he was nineteen. At the Olympics, he finished fourth in the 5,000-meter race, just missing a medal. After retiring from competition, he became a high school teacher and coached young athletes for over thirty years. Several of his students later became national champions.""", 'Oliver Grant',
 ['매니토바의 농장에서 태어났다.', '매일 몇 킬로미터를 달려 등교했다.', '19살이 되어서야 전문적인 훈련을 받았다.', '5,000미터 경주에서 4위를 했다.', '30년 넘게 젊은 선수들을 지도했다.'],
 ['올림픽에서 금메달을 땄다.', '은퇴 후 프로 육상 코치로만 일했다.']),
("""The Venus flytrap is a carnivorous plant that grows naturally only in a small area of North and South Carolina in the United States. Each leaf has two lobes lined with stiff hairs. When an insect touches these hairs twice within about 20 seconds, the leaf snaps shut in less than a second. This double-touch system prevents the plant from wasting energy on raindrops. The plant then digests the insect over about a week. Although it catches insects, the flytrap still uses photosynthesis to make most of its food.""", 'Venus flytrap',
 ['미국 노스·사우스캐롤라이나의 좁은 지역에서만 자생한다.', '잎에 뻣뻣한 털이 나 있다.', '1초도 안 되어 잎을 닫는다.', '곤충을 약 일주일에 걸쳐 소화한다.', '대부분의 양분은 광합성으로 만든다.'],
 ['털이 한 번만 닿아도 잎이 닫힌다.', '곤충을 잡기 때문에 광합성을 하지 않는다.']),
("""Leo Martins was a Brazilian photographer who spent his career documenting the Amazon rainforest. Born in São Paulo in 1960, he first visited the Amazon at the age of twenty-five and decided to stay. He lived with local communities for months at a time, learning their languages and customs. His photographs, which show both the beauty of the forest and the damage caused by logging, have been exhibited in more than thirty countries. In 2015, he founded an organization that plants trees in deforested areas.""", 'Leo Martins',
 ['상파울루에서 태어났다.', '25살에 처음 아마존을 방문했다.', '지역 공동체와 함께 지내며 그들의 언어를 배웠다.', '사진이 30개국 이상에서 전시되었다.', '벌목 지역에 나무를 심는 단체를 설립했다.'],
 ['아마존의 아름다움만을 사진에 담았다.', '아마존을 방문한 뒤 곧바로 도시로 돌아갔다.']),
]

# NOTICES: (안내문, 대상, [일치 5], [불일치 4])  — 27·28번 실용문
NOTICES = [
("""2027 Lakeside Summer Reading Challenge
Read books, earn prizes, and have fun this summer!
■ Who: Students in grades 1–9
■ When: July 1 – August 15
■ How to Participate
- Register at the library front desk or on our website.
- Record each book you read in your reading log.
■ Prizes
- Read 10 books: a free bookmark
- Read 20 books: a T-shirt and a ticket to the closing party
■ Notes
- Audiobooks also count.
- Participation is free.
For more information, visit www.lakesidelib.org.""", 'Lakeside Summer Reading Challenge',
 ['1학년부터 9학년까지 참여할 수 있다.', '7월 1일부터 8월 15일까지 진행된다.', '도서관 안내 데스크나 웹사이트에서 등록할 수 있다.', '오디오북도 읽은 책으로 인정된다.', '참가비는 무료이다.'],
 ['고등학생만 참여할 수 있다.', '10권을 읽으면 티셔츠를 받는다.', '오디오북은 인정되지 않는다.', '참가비를 내야 한다.']),
("""Greenfield Farmers' Market
Fresh, local, and seasonal!
● Open every Saturday from 8 a.m. to 1 p.m. (April – October)
● Location: City Hall Parking Lot
● What You'll Find
- Fruits and vegetables from local farms
- Homemade bread, jam, and cheese
● Special Events
- Cooking demonstrations at 10 a.m. on the first Saturday of each month
● Please Note
- Bring your own shopping bags. Plastic bags are not provided.
- Pets are not allowed in the market area.""", "Greenfield Farmers' Market",
 ['4월부터 10월까지 매주 토요일에 열린다.', '시청 주차장에서 열린다.', '지역 농장의 과일과 채소를 판매한다.', '매달 첫째 토요일에 요리 시연이 있다.', '반려동물은 시장 구역에 들어올 수 없다.'],
 ['매일 아침 문을 연다.', '비닐봉지를 무료로 제공한다.', '요리 시연은 매주 열린다.', '반려동물과 함께 입장할 수 있다.']),
("""Youth Robotics Workshop
Build and program your own robot!
□ Dates: August 5 – 9 (Monday – Friday)
□ Time: 1 p.m. – 4 p.m.
□ Place: Hillside Science Center, Room 201
□ Participants: Ages 12 – 16 (Maximum 20 students)
□ Fee: $80 (All materials included)
□ Registration: Online only, by July 25
※ No experience is necessary.
※ Participants can take their robots home after the workshop.""", 'Youth Robotics Workshop',
 ['5일 동안 진행된다.', '12세부터 16세까지 참가할 수 있다.', '참가비에 모든 재료비가 포함된다.', '온라인으로만 등록할 수 있다.', '워크숍 후 만든 로봇을 집에 가져갈 수 있다.'],
 ['오전에 진행된다.', '참가 인원에는 제한이 없다.', '재료비는 별도로 내야 한다.', '로봇 제작 경험이 있어야 참가할 수 있다.']),
("""Riverside Charity Fun Run
Run for a good cause!
◆ Date: Sunday, September 22
◆ Start Time: 9:00 a.m. at Riverside Park
◆ Courses: 5 km and 10 km
◆ Registration Fee: Adults $20 / Students $10
◆ All proceeds will be donated to the local children's hospital.
◆ Every runner will receive a T-shirt and a medal.
◆ Strollers are welcome on the 5 km course only.
◆ The event will be held rain or shine.""", 'Riverside Charity Fun Run',
 ['리버사이드 공원에서 오전 9시에 출발한다.', '5 km와 10 km 코스가 있다.', '수익금은 지역 어린이 병원에 기부된다.', '모든 참가자는 티셔츠와 메달을 받는다.', '비가 와도 행사는 진행된다.'],
 ['학생 참가비는 20달러이다.', '유모차는 두 코스 모두 이용할 수 있다.', '비가 오면 행사가 취소된다.', '수익금은 참가자에게 돌려준다.']),
("""City Museum Night Tour
Experience the museum after dark!
• Every Friday in October, 7 p.m. – 9 p.m.
• Guided tours start every 30 minutes from the main lobby.
• Ticket Price: $15 (Members: $10)
• Children under 10 must be accompanied by an adult.
• Flash photography is not allowed.
• Tickets can be purchased online or at the door.
• The museum café will stay open until 8:30 p.m.""", 'City Museum Night Tour',
 ['10월 매주 금요일에 진행된다.', '가이드 투어는 30분마다 시작된다.', '회원은 10달러에 입장할 수 있다.', '10세 미만 어린이는 어른과 동반해야 한다.', '박물관 카페는 오후 8시 30분까지 운영된다.'],
 ['투어는 오후 7시에 한 번만 시작된다.', '플래시 사진 촬영이 허용된다.', '입장권은 현장에서 살 수 없다.', '카페는 오후 9시까지 운영된다.']),
("""Spring Photo Contest
Show us spring through your lens!
▶ Theme: 'Signs of Spring in Our Town'
▶ Eligibility: High school students living in Westbrook
▶ Submission Period: April 1 – April 20
▶ Guidelines
- Each person may submit up to two photos.
- Photos must be taken this year.
- Edited photos are not accepted.
▶ Prizes: 1st Place – $200, 2nd Place – $100
▶ Winners will be announced on our website on May 5.""", 'Spring Photo Contest',
 ['웨스트브룩에 사는 고등학생이 참가할 수 있다.', '4월 1일부터 4월 20일까지 제출한다.', '1인당 사진을 두 장까지 제출할 수 있다.', '편집한 사진은 받지 않는다.', '수상자는 5월 5일 웹사이트에 발표된다.'],
 ['참가 자격에 제한이 없다.', '사진은 장수 제한 없이 제출할 수 있다.', '작년에 찍은 사진도 제출할 수 있다.', '1등 상금은 100달러이다.']),
("""Oakwood Community Pool Rules
■ Hours: 6 a.m. – 9 p.m. daily (Closed on the first Monday of each month for cleaning)
■ All swimmers must shower before entering the pool.
■ Children under 8 must be supervised by an adult at all times.
■ Swimming caps are required.
■ Food and drinks are allowed only in the picnic area.
■ Lifeguards are on duty from 9 a.m. to 6 p.m.""", 'Oakwood Community Pool',
 ['매일 오전 6시부터 오후 9시까지 운영한다.', '매달 첫째 월요일은 청소를 위해 문을 닫는다.', '입수 전 샤워를 해야 한다.', '수영모를 반드시 착용해야 한다.', '음식은 피크닉 구역에서만 먹을 수 있다.'],
 ['인명 구조원이 하루 종일 근무한다.', '수영모 착용은 선택 사항이다.', '수영장 가장자리에서 음식을 먹을 수 있다.', '8세 미만 어린이 혼자 수영할 수 있다.']),
("""Hilltop High School Talent Show
Do you sing, dance, or play an instrument? Show your talent!
* Date: Friday, November 15, 6 p.m.
* Place: School Auditorium
* Auditions: November 4 – 6, after school in the music room
* Each performance must be under 5 minutes.
* Both individuals and groups (up to 6 members) may apply.
* Sign up with Mr. Grant in the music office by October 31.
* Admission is free for all students and families.""", 'Hilltop High School Talent Show',
 ['11월 15일 금요일 오후 6시에 열린다.', '오디션은 음악실에서 방과 후에 열린다.', '각 공연은 5분 미만이어야 한다.', '6명까지의 단체도 지원할 수 있다.', '학생과 가족은 무료로 입장할 수 있다.'],
 ['공연 시간에는 제한이 없다.', '개인만 지원할 수 있다.', '10월 31일 이후에도 신청할 수 있다.', '가족은 입장료를 내야 한다.']),
("""Winter Clothing Drive
Help keep our neighbors warm this winter!
● Collection Period: December 1 – December 20
● Drop-off Location: Main entrance of Pinecrest Community Center
● We Accept: Clean coats, sweaters, scarves, gloves, and hats
● We Do Not Accept: Shoes or damaged items
● All donations will be given to local shelters.
● Volunteers are needed to sort clothes on weekends. Contact Ms. Reed at 555-0192.""", 'Winter Clothing Drive',
 ['12월 1일부터 12월 20일까지 물품을 모은다.', '파인크레스트 커뮤니티 센터 정문에서 물품을 받는다.', '깨끗한 외투와 장갑을 기부할 수 있다.', '기부품은 지역 보호 시설에 전달된다.', '주말에 옷을 분류할 자원봉사자가 필요하다.'],
 ['신발도 기부할 수 있다.', '손상된 물품도 받는다.', '기부품은 해외로 보내진다.', '자원봉사자는 평일에만 필요하다.']),
("""Starlight Observatory Open Night
Look at the stars through our giant telescope!
- Date: Saturday, March 9 (In case of clouds or rain, it will be moved to March 16.)
- Time: 8 p.m. – 10 p.m.
- Admission: Free (Reservation required)
- Reservations open on February 25 through our website.
- Each reservation is limited to 4 people.
- Warm clothing is recommended, as the observation deck is outdoors.""", 'Starlight Observatory Open Night',
 ['구름이 끼거나 비가 오면 3월 16일로 연기된다.', '오후 8시부터 10시까지 진행된다.', '입장료는 무료이다.', '예약은 1건당 4명으로 제한된다.', '관측 데크는 야외에 있다.'],
 ['예약 없이 입장할 수 있다.', '날씨와 관계없이 3월 9일에 진행된다.', '예약은 전화로만 받는다.', '관측 데크는 실내에 있다.']),
("""Maple Valley Bike Rental
Explore the valley on two wheels!
◇ Open: 9 a.m. – 6 p.m. (March – November)
◇ Rental Fees: 1 hour – $8 / Full day – $30
◇ Helmets are provided free of charge.
◇ Riders under 14 must wear a helmet and be accompanied by an adult.
◇ A valid ID is required to rent a bike.
◇ Bikes must be returned by 6 p.m.; late returns will be charged $10.""", 'Maple Valley Bike Rental',
 ['3월부터 11월까지 운영한다.', '하루 대여료는 30달러이다.', '헬멧은 무료로 제공된다.', '자전거를 빌리려면 신분증이 필요하다.', '늦게 반납하면 10달러를 내야 한다.'],
 ['1년 내내 운영한다.', '헬멧 대여료가 따로 있다.', '14세 미만은 혼자 자전거를 탈 수 있다.', '반납 시간에는 제한이 없다.']),
("""Teen Cooking Class: Healthy Snacks
Learn to make tasty and healthy snacks!
○ For: Ages 13 – 18
○ Date: Every Saturday in June, 10 a.m. – 12 p.m.
○ Place: Sunrise Community Kitchen
○ Fee: $40 for all four classes
○ Participants should bring an apron.
○ Please tell us about any food allergies when you register.
○ Class size is limited to 12 students.""", 'Teen Cooking Class',
 ['13세부터 18세까지 참여할 수 있다.', '6월 매주 토요일 오전에 진행된다.', '네 번의 수업 전체 비용은 40달러이다.', '참가자는 앞치마를 가져와야 한다.', '정원은 12명이다.'],
 ['수업은 오후에 진행된다.', '앞치마는 무료로 제공된다.', '한 번 수업 비용이 40달러이다.', '정원 제한이 없다.']),
("""Hanbit Middle & High School Library: Exam Period Hours
To support students preparing for final exams, the library will extend its opening hours.
■ Period: June 17 – June 28
■ Weekdays: 7:30 a.m. – 9:00 p.m.
■ Saturdays: 9:00 a.m. – 5:00 p.m. (Closed on Sundays)
■ Study rooms can be reserved for up to two hours per day.
■ Eating is not allowed, but water in a closed bottle is permitted.
■ Please keep your phone on silent mode.""", 'library exam period hours',
 ['기말고사 준비를 위해 운영 시간을 연장한다.', '평일에는 오후 9시까지 운영한다.', '일요일에는 문을 닫는다.', '스터디룸은 하루 최대 2시간 예약할 수 있다.', '뚜껑이 있는 병에 든 물은 허용된다.'],
 ['토요일에는 문을 닫는다.', '스터디룸은 시간 제한 없이 쓸 수 있다.', '음식을 먹을 수 있다.', '일요일에도 운영한다.']),
("""Paper Airplane Contest
Fly your best paper airplane!
◎ Date: Saturday, May 18, 2 p.m.
◎ Place: Westside Gym
◎ Categories: Longest Distance / Longest Flight Time
◎ Rules
- Use only one sheet of A4 paper.
- No tape, glue, or scissors are allowed.
- Each participant gets three throws.
◎ Winners of each category will receive a gift card.
◎ Open to all ages. No registration needed.""", 'Paper Airplane Contest',
 ['5월 18일 오후 2시에 열린다.', '최장 거리와 최장 비행 시간 부문이 있다.', 'A4 용지 한 장만 사용해야 한다.', '참가자마다 세 번 던질 수 있다.', '사전 등록이 필요 없다.'],
 ['테이프를 사용할 수 있다.', '참가자는 한 번만 던질 수 있다.', '학생만 참가할 수 있다.', '반드시 사전 등록해야 한다.']),
]
