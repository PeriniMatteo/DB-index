
##Visualizzare tutte le domande e le risposte per un determinato paese e INDEX

SELECT Common_name, Article_number, Article_Field, Question_section, Question_number, Question_text, Answere_Score

FROM indexdb.Articles, indexdb.Answers, indexdb.Questions,indexdb.Countries, indexdb.Inquiries, indexdb.QuestionInAssesment, indexdb.Assesment

WHERE Common_name='Romania' and Assesment_Name='Index2015' and Countries_idCountries=idCountries and Inquiries_idInquiries=idInquiries and idQuestions = Questions_idQuestions and idQIA = QuestionInAssesment_idQIA and idArticles = Articles_idArticles

##Visualizzare tutte le domande e le risposte per un determinato paese e INDEX appartenenti ad es a "SERVICES"

SELECT Common_name, Article_number, Article_Field, Question_section, Question_number, Question_text, Answere_Score

FROM indexdb.Articles, indexdb.Answers, indexdb.Questions,indexdb.Countries, indexdb.Inquiries, indexdb.QuestionInAssesment, indexdb.Assesment

WHERE Common_name='Romania' and Assesment_Name='Index2015' and Countries_idCountries=idCountries and Inquiries_idInquiries=idInquiries and idQuestions = Questions_idQuestions and idQIA = QuestionInAssesment_idQIA and idArticles = Articles_idArticles and Question_section='SERVICES'

##Visualizzare tutte le domande e le risposte per un determinato paese e INDEX appartenenti ad es all'argomento "Adoption"

select Common_name,Article_number,Article_Field,Question_section,Question_number,Question_text,Answere_Score
from indexdb.Articles, indexdb.Answers, indexdb.Questions,indexdb.Countries, indexdb.Inquiries, indexdb.QuestionInAssesment, indexdb.Assesment
WHERE Common_name='Romania' and Assesment_Name='Index2015' and Countries_idCountries=idCountries and Inquiries_idInquiries=idInquiries and idAssesment=Assesment_idAssesment
and idQuestions = Questions_idQuestions and idQIA = QuestionInAssesment_idQIA and idArticles = Articles_idArticles and Article_Field="Adoption"

##Visualizzare tutte le domande e le risposte per tutti i paesi ad un INDEX ordinati per articolo,sezione,numero

select Common_name,Article_number,Article_Field,Question_section,Question_number,Question_text,Answere_Score
from indexdb.Articles, indexdb.Answers, indexdb.Questions,indexdb.Countries, indexdb.Inquiries, indexdb.QuestionInAssesment, indexdb.Assesment
WHERE Assesment_Name='Index2015' and Countries_idCountries=idCountries and Inquiries_idInquiries=idInquiries and idAssesment=Assesment_idAssesment
and idQuestions = Questions_idQuestions and idQIA = QuestionInAssesment_idQIA and idArticles = Articles_idArticles 
ORDER BY Article_number, Question_section, Question_number;

##Visualizzare tutte le domande e le risposte di 2 paesi ad un INDEX e ad un solo articolo (38) ordinati 

select Common_name,Article_number,Article_Field,Question_section,Question_number,Question_text,Answere_Score
from indexdb.Articles, indexdb.Answers, indexdb.Questions,indexdb.Countries, indexdb.Inquiries, indexdb.QuestionInAssesment, indexdb.Assesment
WHERE Assesment_Name='Index2015' and Countries_idCountries=idCountries and Inquiries_idInquiries=idInquiries and idAssesment=Assesment_idAssesment
and idQuestions = Questions_idQuestions and idQIA = QuestionInAssesment_idQIA and idArticles = Articles_idArticles and Common_name IN ('Moldova','Romania') and Article_number=38
ORDER BY Article_number, Question_section, Question_number;

##Visualizza le domande e risposte di tutti i paesi ad un INDEX e ad una sola domanda 

select Common_name,Article_number,Article_Field,Question_section,Question_number,Question_text,Answere_Score
from indexdb.Articles, indexdb.Answers, indexdb.Questions,indexdb.Countries, indexdb.Inquiries, indexdb.QuestionInAssesment, indexdb.Assesment
WHERE Assesment_Name='Index2015' and Countries_idCountries=idCountries and Inquiries_idInquiries=idInquiries and idAssesment=Assesment_idAssesment
and idQuestions = Questions_idQuestions and idQIA = QuestionInAssesment_idQIA and idArticles = Articles_idArticles and Article_number=19 and Question_number=3 and Question_section='ACCOUNTABILITY'

