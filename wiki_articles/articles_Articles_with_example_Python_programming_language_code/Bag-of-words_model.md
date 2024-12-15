# Bag-of-words model

## Article Metadata

- **Last Updated:** 2024-12-15T03:43:31.809305+00:00
- **Original Article:** [Bag-of-words model](https://en.wikipedia.org/wiki/Bag-of-words_model)
- **Language:** en
- **Page ID:** 14003441

## Summary

The bag-of-words model (BoW) is a model of text which uses a representation of text that is based on an unordered collection (a "bag") of words. It is used in natural language processing and information retrieval (IR). It disregards word order (and thus most of syntax or grammar) but captures multiplicity.
The bag-of-words model is commonly used in methods of document classification where, for example, the (frequency of) occurrence of each word is used as a feature for training a classifier. It 

## Categories

- Category:Articles with example Python (programming language) code
- Category:Articles with short description
- Category:Machine learning
- Category:Natural language processing
- Category:Short description is different from Wikidata
- Category:Wikipedia articles needing clarification from December 2023

## Table of Contents

- Definition
- Implementations
- Python implementation
- Hashing trick
- See also
- Notes
- References

## Content

The bag-of-words model (BoW) is a model of text which uses a representation of text that is based on an unordered collection (a "bag") of words. It is used in natural language processing and information retrieval (IR). It disregards word order (and thus most of syntax or grammar) but captures multiplicity.
The bag-of-words model is commonly used in methods of document classification where, for example, the (frequency of) occurrence of each word is used as a feature for training a classifier. It has also been used for computer vision.
An early reference to "bag of words" in a linguistic context can be found in Zellig Harris's 1954 article on Distributional Structure.

Definition
The following models a text document using bag-of-words. Here are two simple text documents:

Based on these two text documents, a list is constructed as follows for each document:

Representing each bag-of-words as a JSON object, and attributing to the respective JavaScript variable:

Each key is the word, and each value is the number of occurrences of that word in the given text document.
The order of elements is free, so, for example {"too":1,"Mary":1,"movies":2,"John":1,"watch":1,"likes":2,"to":1} is also equivalent to BoW1. It is also what we expect from a strict JSON object representation.
Note: if another document is like a union of these two,

its JavaScript representation will be:

So, as we see in the bag algebra, the "union" of two documents in the bags-of-words representation is, formally, the disjoint union, summing the multiplicities of each element.
  
    
      
        B
        o
        W
        3
        =
        B
        o
        W
        1
        ⨄
        B
        o
        W
        2
      
    
    {\displaystyle BoW3=BoW1\biguplus BoW2}

Word order
The BoW representation of a text removes all word ordering. For example, the BoW representation of "man bites dog" and "dog bites man" are the same, so any algorithm that operates with a BoW representation of text must treat them in the same way. Despite this lack of syntax or grammar, BoW representation is fast and may be sufficient for simple tasks that do not require word order. For instance, for document classification, if the words "stocks" "trade" "investors" appears multiple times, then the text is likely a financial report, even though it would be insufficient to distinguish between Yesterday, investors were rallying, but today, they are retreating.andYesterday, investors were retreating, but today, they are rallying.and so the BoW representation would be insufficient to determine the detailed meaning of the document.

Implementations
Implementations of the bag-of-words model might involve using frequencies of words in a document to represent its contents. The frequencies can be "normalized" by the inverse of document frequency, or tf–idf. Additionally, for the specific purpose of classification, supervised alternatives have been developed to account for the class label of a document. Lastly, binary (presence/absence or 1/0) weighting is used in place of frequencies for some problems (e.g., this option is implemented in the WEKA machine learning software system).

Python implementation
Hashing trick
A common alternative to using dictionaries is the hashing trick, where words are mapped directly to indices with a hashing function. Thus, no memory is required to store a dictionary. Hash collisions are typically dealt via freed-up memory to increase the number of hash buckets. In practice, hashing simplifies the implementation of bag-of-words models and improves scalability.

See also
Additive smoothing
Feature extraction
Machine learning
MinHash
Vector space model
w-shingling

Notes
References
McTear, Michael (et al) (2016). The Conversational Interface. Springer International Publishing.

## Related Articles

### Internal Links

- [AI-complete](https://en.wikipedia.org/wiki/AI-complete)
- [Additive smoothing](https://en.wikipedia.org/wiki/Additive_smoothing)
- [ArXiv](https://en.wikipedia.org/wiki/ArXiv)
- [Argument mining](https://en.wikipedia.org/wiki/Argument_mining)
- [Association for Computing Machinery](https://en.wikipedia.org/wiki/Association_for_Computing_Machinery)
- [Automated essay scoring](https://en.wikipedia.org/wiki/Automated_essay_scoring)
- [Automatic identification and data capture](https://en.wikipedia.org/wiki/Automatic_identification_and_data_capture)
- [Automatic summarization](https://en.wikipedia.org/wiki/Automatic_summarization)
- [BERT (language model)](https://en.wikipedia.org/wiki/BERT_(language_model))
- [BabelNet](https://en.wikipedia.org/wiki/BabelNet)
- [Bag-of-words model in computer vision](https://en.wikipedia.org/wiki/Bag-of-words_model_in_computer_vision)
- [Bank of English](https://en.wikipedia.org/wiki/Bank_of_English)
- [Bibcode](https://en.wikipedia.org/wiki/Bibcode)
- [Bigram](https://en.wikipedia.org/wiki/Bigram)
- [Chatbot](https://en.wikipedia.org/wiki/Chatbot)
- [Collocation extraction](https://en.wikipedia.org/wiki/Collocation_extraction)
- [Compound-term processing](https://en.wikipedia.org/wiki/Compound-term_processing)
- [Computational linguistics](https://en.wikipedia.org/wiki/Computational_linguistics)
- [Computer-assisted reviewing](https://en.wikipedia.org/wiki/Computer-assisted_reviewing)
- [Computer-assisted translation](https://en.wikipedia.org/wiki/Computer-assisted_translation)
- [Concept mining](https://en.wikipedia.org/wiki/Concept_mining)
- [Concordancer](https://en.wikipedia.org/wiki/Concordancer)
- [Coreference](https://en.wikipedia.org/wiki/Coreference)
- [Corpus linguistics](https://en.wikipedia.org/wiki/Corpus_linguistics)
- [DBpedia](https://en.wikipedia.org/wiki/DBpedia)
- [Deep linguistic processing](https://en.wikipedia.org/wiki/Deep_linguistic_processing)
- [Disjoint union](https://en.wikipedia.org/wiki/Disjoint_union)
- [Distant reading](https://en.wikipedia.org/wiki/Distant_reading)
- [Distributional semantics](https://en.wikipedia.org/wiki/Distributional_semantics)
- [Document-term matrix](https://en.wikipedia.org/wiki/Document-term_matrix)
- [Document classification](https://en.wikipedia.org/wiki/Document_classification)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Example-based machine translation](https://en.wikipedia.org/wiki/Example-based_machine_translation)
- [Explicit semantic analysis](https://en.wikipedia.org/wiki/Explicit_semantic_analysis)
- [FastText](https://en.wikipedia.org/wiki/FastText)
- [Feature (machine learning)](https://en.wikipedia.org/wiki/Feature_(machine_learning))
- [Feature engineering](https://en.wikipedia.org/wiki/Feature_engineering)
- [Formal semantics (natural language)](https://en.wikipedia.org/wiki/Formal_semantics_(natural_language))
- [FrameNet](https://en.wikipedia.org/wiki/FrameNet)
- [GloVe](https://en.wikipedia.org/wiki/GloVe)
- [Google Books Ngram Viewer](https://en.wikipedia.org/wiki/Google_Books_Ngram_Viewer)
- [Grammar checker](https://en.wikipedia.org/wiki/Grammar_checker)
- [Hallucination (artificial intelligence)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))
- [Feature hashing](https://en.wikipedia.org/wiki/Feature_hashing)
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Information extraction](https://en.wikipedia.org/wiki/Information_extraction)
- [Information retrieval](https://en.wikipedia.org/wiki/Information_retrieval)
- [Interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction)
- [JSON](https://en.wikipedia.org/wiki/JSON)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Language model](https://en.wikipedia.org/wiki/Language_model)
- [Language resource](https://en.wikipedia.org/wiki/Language_resource)
- [Large language model](https://en.wikipedia.org/wiki/Large_language_model)
- [Latent Dirichlet allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)
- [Latent semantic analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis)
- [Lemmatization](https://en.wikipedia.org/wiki/Lemmatization)
- [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
- [Lexical resource](https://en.wikipedia.org/wiki/Lexical_resource)
- [Linguistic Linked Open Data](https://en.wikipedia.org/wiki/Linguistic_Linked_Open_Data)
- [Machine-readable dictionary](https://en.wikipedia.org/wiki/Machine-readable_dictionary)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Machine translation](https://en.wikipedia.org/wiki/Machine_translation)
- [Man bites dog](https://en.wikipedia.org/wiki/Man_bites_dog)
- [MinHash](https://en.wikipedia.org/wiki/MinHash)
- [Multi-document summarization](https://en.wikipedia.org/wiki/Multi-document_summarization)
- [Multiplicity (mathematics)](https://en.wikipedia.org/wiki/Multiplicity_(mathematics))
- [Multiset](https://en.wikipedia.org/wiki/Multiset)
- [N-gram](https://en.wikipedia.org/wiki/N-gram)
- [Named-entity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)
- [Natural-language user interface](https://en.wikipedia.org/wiki/Natural-language_user_interface)
- [Natural Language Toolkit](https://en.wikipedia.org/wiki/Natural_Language_Toolkit)
- [Natural language generation](https://en.wikipedia.org/wiki/Natural_language_generation)
- [Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Natural language understanding](https://en.wikipedia.org/wiki/Natural_language_understanding)
- [Neural machine translation](https://en.wikipedia.org/wiki/Neural_machine_translation)
- [Ontology learning](https://en.wikipedia.org/wiki/Ontology_learning)
- [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition)
- [Pachinko allocation](https://en.wikipedia.org/wiki/Pachinko_allocation)
- [Parallel text](https://en.wikipedia.org/wiki/Parallel_text)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Part-of-speech tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging)
- [Predictive text](https://en.wikipedia.org/wiki/Predictive_text)
- [Pronunciation assessment](https://en.wikipedia.org/wiki/Pronunciation_assessment)
- [PropBank](https://en.wikipedia.org/wiki/PropBank)
- [Question answering](https://en.wikipedia.org/wiki/Question_answering)
- [Rule-based machine translation](https://en.wikipedia.org/wiki/Rule-based_machine_translation)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [Semantic analysis (machine learning)](https://en.wikipedia.org/wiki/Semantic_analysis_(machine_learning))
- [Semantic decomposition (natural language processing)](https://en.wikipedia.org/wiki/Semantic_decomposition_(natural_language_processing))
- [Semantic network](https://en.wikipedia.org/wiki/Semantic_network)
- [Semantic parsing](https://en.wikipedia.org/wiki/Semantic_parsing)
- [Semantic role labeling](https://en.wikipedia.org/wiki/Semantic_role_labeling)
- [Semantic similarity](https://en.wikipedia.org/wiki/Semantic_similarity)
- [Sentence boundary disambiguation](https://en.wikipedia.org/wiki/Sentence_boundary_disambiguation)
- [Sentence extraction](https://en.wikipedia.org/wiki/Sentence_extraction)
- [Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis)
- [Seq2seq](https://en.wikipedia.org/wiki/Seq2seq)
- [Shallow parsing](https://en.wikipedia.org/wiki/Shallow_parsing)
- [Simple Knowledge Organization System](https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System)
- [SpaCy](https://en.wikipedia.org/wiki/SpaCy)
- [Special Interest Group on Information Retrieval](https://en.wikipedia.org/wiki/Special_Interest_Group_on_Information_Retrieval)
- [Speech corpus](https://en.wikipedia.org/wiki/Speech_corpus)
- [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition)
- [Speech segmentation](https://en.wikipedia.org/wiki/Speech_segmentation)
- [Speech synthesis](https://en.wikipedia.org/wiki/Speech_synthesis)
- [Spell checker](https://en.wikipedia.org/wiki/Spell_checker)
- [Statistical classification](https://en.wikipedia.org/wiki/Statistical_classification)
- [Statistical machine translation](https://en.wikipedia.org/wiki/Statistical_machine_translation)
- [Stemming](https://en.wikipedia.org/wiki/Stemming)
- [Stop word](https://en.wikipedia.org/wiki/Stop_word)
- [Supervised learning](https://en.wikipedia.org/wiki/Supervised_learning)
- [Syntactic parsing (computational linguistics)](https://en.wikipedia.org/wiki/Syntactic_parsing_(computational_linguistics))
- [MUD terminology](https://en.wikipedia.org/wiki/MUD_terminology)
- [Terminology extraction](https://en.wikipedia.org/wiki/Terminology_extraction)
- [Text corpus](https://en.wikipedia.org/wiki/Text_corpus)
- [Text mining](https://en.wikipedia.org/wiki/Text_mining)
- [Text processing](https://en.wikipedia.org/wiki/Text_processing)
- [Text segmentation](https://en.wikipedia.org/wiki/Text_segmentation)
- [Text simplification](https://en.wikipedia.org/wiki/Text_simplification)
- [Textual entailment](https://en.wikipedia.org/wiki/Textual_entailment)
- [Tf–idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
- [Thesaurus (information retrieval)](https://en.wikipedia.org/wiki/Thesaurus_(information_retrieval))
- [Topic model](https://en.wikipedia.org/wiki/Topic_model)
- [Transfer-based machine translation](https://en.wikipedia.org/wiki/Transfer-based_machine_translation)
- [Treebank](https://en.wikipedia.org/wiki/Treebank)
- [Trigram](https://en.wikipedia.org/wiki/Trigram)
- [Truecasing](https://en.wikipedia.org/wiki/Truecasing)
- [UBY](https://en.wikipedia.org/wiki/UBY)
- [Universal Dependencies](https://en.wikipedia.org/wiki/Universal_Dependencies)
- [Vector space model](https://en.wikipedia.org/wiki/Vector_space_model)
- [Virtual assistant](https://en.wikipedia.org/wiki/Virtual_assistant)
- [Voice user interface](https://en.wikipedia.org/wiki/Voice_user_interface)
- [W-shingling](https://en.wikipedia.org/wiki/W-shingling)
- [Weka (software)](https://en.wikipedia.org/wiki/Weka_(software))
- [Wikidata](https://en.wikipedia.org/wiki/Wikidata)
- [Word](https://en.wikipedia.org/wiki/Word)
- [Word-sense disambiguation](https://en.wikipedia.org/wiki/Word-sense_disambiguation)
- [Word-sense induction](https://en.wikipedia.org/wiki/Word-sense_induction)
- [Word2vec](https://en.wikipedia.org/wiki/Word2vec)
- [WordNet](https://en.wikipedia.org/wiki/WordNet)
- [Word embedding](https://en.wikipedia.org/wiki/Word_embedding)
- [Word order](https://en.wikipedia.org/wiki/Word_order)
- [Zellig Harris](https://en.wikipedia.org/wiki/Zellig_Harris)
- [Wikipedia:Please clarify](https://en.wikipedia.org/wiki/Wikipedia:Please_clarify)
- [Template:Natural language processing](https://en.wikipedia.org/wiki/Template:Natural_language_processing)
- [Template talk:Natural language processing](https://en.wikipedia.org/wiki/Template_talk:Natural_language_processing)
- [Category:Wikipedia articles needing clarification from December 2023](https://en.wikipedia.org/wiki/Category:Wikipedia_articles_needing_clarification_from_December_2023)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T03:43:31.809305+00:00_