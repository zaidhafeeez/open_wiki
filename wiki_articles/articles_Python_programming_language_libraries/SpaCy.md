# SpaCy

## Article Metadata

- **Last Updated:** 2024-12-15T04:08:25.137134+00:00
- **Original Article:** [SpaCy](https://en.wikipedia.org/wiki/SpaCy)
- **Language:** en
- **Page ID:** 52630840

## Summary

spaCy ( spay-SEE) is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython. The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion.
Unlike NLTK, which is widely used for teaching and research, spaCy focuses on providing software for production usage. spaCy also supports deep learning workflows that allow connecting statis

## Categories

- Category:2015 software
- Category:Articles with short description
- Category:Free science software
- Category:Natural language processing toolkits
- Category:Python (programming language) libraries
- Category:Short description matches Wikidata

## Table of Contents

- History
- Main features
- Extensions and visualizers
- References
- External links

## Content

spaCy ( spay-SEE) is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython. The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion.
Unlike NLTK, which is widely used for teaching and research, spaCy focuses on providing software for production usage. spaCy also supports deep learning workflows that allow connecting statistical models trained by popular machine learning libraries like TensorFlow, PyTorch or MXNet through its own machine learning library Thinc. Using Thinc as its backend, spaCy features convolutional neural network models for part-of-speech tagging, dependency parsing, text categorization and named entity recognition (NER). Prebuilt statistical neural network models to perform these tasks are available for 23 languages, including English, Portuguese, Spanish, Russian and Chinese, and there is also a multi-language NER model. Additional support for tokenization for more than 65 languages allows users to train custom models on their own datasets as well.

History
Version 1.0 was released on October 19, 2016, and included preliminary support for deep learning workflows by supporting custom processing pipelines. It further included a rule matcher that supported entity annotations, and an officially documented training API.
Version 2.0 was released on November 7, 2017, and introduced convolutional neural network models for 7 different languages. It also supported custom processing pipeline components and extension attributes, and featured a built-in trainable text classification component.
Version 3.0 was released on February 1, 2021, and introduced state-of-the-art transformer-based pipelines. It also introduced a new configuration system and training workflow, as well as type hints and project templates. This version dropped support for Python 2.

Main features
Non-destructive tokenization
"Alpha tokenization" support for over 65 languages
Built-in support for trainable pipeline components such as Named entity recognition, Part-of-speech tagging, dependency parsing, Text classification, Entity Linking and more
Statistical models for 19 languages
Multi-task learning with pretrained transformers like BERT
Support for custom models in PyTorch, TensorFlow and other frameworks
State-of-the-art speed and accuracy
Production-ready training system
Built-in visualizers for syntax and named entities
Easy model packaging, deployment and workflow management

Extensions and visualizers
spaCy comes with several extensions and visualizations that are available as free, open-source libraries: 

Thinc: A machine learning library optimized for CPU usage and deep learning with text input.
sense2vec: A library for computing word similarities, based on Word2vec.
displaCy: An open-source dependency parse tree visualizer built with JavaScript, CSS and SVG.
displaCyENT: An open-source named entity visualizer built with JavaScript and CSS.

References
External links
Official website 
Implementing Spacy Library

## Related Articles

### Internal Links

- [AI-complete](https://en.wikipedia.org/wiki/AI-complete)
- [Apache MXNet](https://en.wikipedia.org/wiki/Apache_MXNet)
- [Argument mining](https://en.wikipedia.org/wiki/Argument_mining)
- [Neural network (machine learning)](https://en.wikipedia.org/wiki/Neural_network_(machine_learning))
- [Automated essay scoring](https://en.wikipedia.org/wiki/Automated_essay_scoring)
- [Automatic identification and data capture](https://en.wikipedia.org/wiki/Automatic_identification_and_data_capture)
- [Automatic summarization](https://en.wikipedia.org/wiki/Automatic_summarization)
- [BERT (language model)](https://en.wikipedia.org/wiki/BERT_(language_model))
- [BabelNet](https://en.wikipedia.org/wiki/BabelNet)
- [Bag-of-words model](https://en.wikipedia.org/wiki/Bag-of-words_model)
- [Bank of English](https://en.wikipedia.org/wiki/Bank_of_English)
- [Bigram](https://en.wikipedia.org/wiki/Bigram)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Central processing unit](https://en.wikipedia.org/wiki/Central_processing_unit)
- [Chatbot](https://en.wikipedia.org/wiki/Chatbot)
- [Collocation extraction](https://en.wikipedia.org/wiki/Collocation_extraction)
- [Compound-term processing](https://en.wikipedia.org/wiki/Compound-term_processing)
- [Computational linguistics](https://en.wikipedia.org/wiki/Computational_linguistics)
- [Computer-assisted reviewing](https://en.wikipedia.org/wiki/Computer-assisted_reviewing)
- [Computer-assisted translation](https://en.wikipedia.org/wiki/Computer-assisted_translation)
- [Computing platform](https://en.wikipedia.org/wiki/Computing_platform)
- [Concept mining](https://en.wikipedia.org/wiki/Concept_mining)
- [Concordancer](https://en.wikipedia.org/wiki/Concordancer)
- [Convolutional neural network](https://en.wikipedia.org/wiki/Convolutional_neural_network)
- [Coreference](https://en.wikipedia.org/wiki/Coreference)
- [Corpus linguistics](https://en.wikipedia.org/wiki/Corpus_linguistics)
- [Cross-platform software](https://en.wikipedia.org/wiki/Cross-platform_software)
- [Cython](https://en.wikipedia.org/wiki/Cython)
- [DBpedia](https://en.wikipedia.org/wiki/DBpedia)
- [Deep learning](https://en.wikipedia.org/wiki/Deep_learning)
- [Deep linguistic processing](https://en.wikipedia.org/wiki/Deep_linguistic_processing)
- [Dependency grammar](https://en.wikipedia.org/wiki/Dependency_grammar)
- [Distant reading](https://en.wikipedia.org/wiki/Distant_reading)
- [Distributional semantics](https://en.wikipedia.org/wiki/Distributional_semantics)
- [Document-term matrix](https://en.wikipedia.org/wiki/Document-term_matrix)
- [Document classification](https://en.wikipedia.org/wiki/Document_classification)
- [Digital object identifier](https://en.wikipedia.org/wiki/Digital_object_identifier)
- [Entity linking](https://en.wikipedia.org/wiki/Entity_linking)
- [Example-based machine translation](https://en.wikipedia.org/wiki/Example-based_machine_translation)
- [Explicit semantic analysis](https://en.wikipedia.org/wiki/Explicit_semantic_analysis)
- [FastText](https://en.wikipedia.org/wiki/FastText)
- [Formal semantics (natural language)](https://en.wikipedia.org/wiki/Formal_semantics_(natural_language))
- [FrameNet](https://en.wikipedia.org/wiki/FrameNet)
- [GloVe](https://en.wikipedia.org/wiki/GloVe)
- [Google Books Ngram Viewer](https://en.wikipedia.org/wiki/Google_Books_Ngram_Viewer)
- [Grammar checker](https://en.wikipedia.org/wiki/Grammar_checker)
- [Hallucination (artificial intelligence)](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))
- [ISBN](https://en.wikipedia.org/wiki/ISBN)
- [Information extraction](https://en.wikipedia.org/wiki/Information_extraction)
- [Interactive fiction](https://en.wikipedia.org/wiki/Interactive_fiction)
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
- [Linux](https://en.wikipedia.org/wiki/Linux)
- [MIT License](https://en.wikipedia.org/wiki/MIT_License)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Machine-readable dictionary](https://en.wikipedia.org/wiki/Machine-readable_dictionary)
- [Machine learning](https://en.wikipedia.org/wiki/Machine_learning)
- [Machine translation](https://en.wikipedia.org/wiki/Machine_translation)
- [Microsoft Windows](https://en.wikipedia.org/wiki/Microsoft_Windows)
- [Multi-document summarization](https://en.wikipedia.org/wiki/Multi-document_summarization)
- [Multi-task learning](https://en.wikipedia.org/wiki/Multi-task_learning)
- [N-gram](https://en.wikipedia.org/wiki/N-gram)
- [Named-entity recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)
- [Named entity](https://en.wikipedia.org/wiki/Named_entity)
- [Natural-language user interface](https://en.wikipedia.org/wiki/Natural-language_user_interface)
- [Natural Language Toolkit](https://en.wikipedia.org/wiki/Natural_Language_Toolkit)
- [Natural language generation](https://en.wikipedia.org/wiki/Natural_language_generation)
- [Natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Natural language understanding](https://en.wikipedia.org/wiki/Natural_language_understanding)
- [Neural machine translation](https://en.wikipedia.org/wiki/Neural_machine_translation)
- [MacOS](https://en.wikipedia.org/wiki/MacOS)
- [Ontology learning](https://en.wikipedia.org/wiki/Ontology_learning)
- [Open-source software](https://en.wikipedia.org/wiki/Open-source_software)
- [Operating system](https://en.wikipedia.org/wiki/Operating_system)
- [Optical character recognition](https://en.wikipedia.org/wiki/Optical_character_recognition)
- [Pachinko allocation](https://en.wikipedia.org/wiki/Pachinko_allocation)
- [Parallel text](https://en.wikipedia.org/wiki/Parallel_text)
- [Parse tree](https://en.wikipedia.org/wiki/Parse_tree)
- [Parsing](https://en.wikipedia.org/wiki/Parsing)
- [Part-of-speech tagging](https://en.wikipedia.org/wiki/Part-of-speech_tagging)
- [Predictive text](https://en.wikipedia.org/wiki/Predictive_text)
- [Programmer](https://en.wikipedia.org/wiki/Programmer)
- [Pronunciation assessment](https://en.wikipedia.org/wiki/Pronunciation_assessment)
- [PropBank](https://en.wikipedia.org/wiki/PropBank)
- [PyTorch](https://en.wikipedia.org/wiki/PyTorch)
- [Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language))
- [History of Python](https://en.wikipedia.org/wiki/History_of_Python)
- [Question answering](https://en.wikipedia.org/wiki/Question_answering)
- [Repository (version control)](https://en.wikipedia.org/wiki/Repository_(version_control))
- [Rule-based machine translation](https://en.wikipedia.org/wiki/Rule-based_machine_translation)
- [Semantic Scholar](https://en.wikipedia.org/wiki/Semantic_Scholar)
- [SVG](https://en.wikipedia.org/wiki/SVG)
- [Scapy](https://en.wikipedia.org/wiki/Scapy)
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
- [Software categories](https://en.wikipedia.org/wiki/Software_categories)
- [Software license](https://en.wikipedia.org/wiki/Software_license)
- [Software release life cycle](https://en.wikipedia.org/wiki/Software_release_life_cycle)
- [Spacy (film)](https://en.wikipedia.org/wiki/Spacy_(film))
- [Speech corpus](https://en.wikipedia.org/wiki/Speech_corpus)
- [Speech recognition](https://en.wikipedia.org/wiki/Speech_recognition)
- [Speech segmentation](https://en.wikipedia.org/wiki/Speech_segmentation)
- [Speech synthesis](https://en.wikipedia.org/wiki/Speech_synthesis)
- [Spell checker](https://en.wikipedia.org/wiki/Spell_checker)
- [Statistical machine translation](https://en.wikipedia.org/wiki/Statistical_machine_translation)
- [Statistical model](https://en.wikipedia.org/wiki/Statistical_model)
- [Stemming](https://en.wikipedia.org/wiki/Stemming)
- [Stop word](https://en.wikipedia.org/wiki/Stop_word)
- [Syntactic parsing (computational linguistics)](https://en.wikipedia.org/wiki/Syntactic_parsing_(computational_linguistics))
- [Syntax](https://en.wikipedia.org/wiki/Syntax)
- [MUD terminology](https://en.wikipedia.org/wiki/MUD_terminology)
- [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow)
- [Terminology extraction](https://en.wikipedia.org/wiki/Terminology_extraction)
- [Document classification](https://en.wikipedia.org/wiki/Document_classification)
- [Document classification](https://en.wikipedia.org/wiki/Document_classification)
- [Text corpus](https://en.wikipedia.org/wiki/Text_corpus)
- [Text mining](https://en.wikipedia.org/wiki/Text_mining)
- [Text processing](https://en.wikipedia.org/wiki/Text_processing)
- [Text segmentation](https://en.wikipedia.org/wiki/Text_segmentation)
- [Text simplification](https://en.wikipedia.org/wiki/Text_simplification)
- [Textual entailment](https://en.wikipedia.org/wiki/Textual_entailment)
- [Thesaurus (information retrieval)](https://en.wikipedia.org/wiki/Thesaurus_(information_retrieval))
- [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
- [Lexical analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
- [Topic model](https://en.wikipedia.org/wiki/Topic_model)
- [Transfer-based machine translation](https://en.wikipedia.org/wiki/Transfer-based_machine_translation)
- [Transformer (deep learning architecture)](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture))
- [Treebank](https://en.wikipedia.org/wiki/Treebank)
- [Trigram](https://en.wikipedia.org/wiki/Trigram)
- [Truecasing](https://en.wikipedia.org/wiki/Truecasing)
- [UBY](https://en.wikipedia.org/wiki/UBY)
- [Universal Dependencies](https://en.wikipedia.org/wiki/Universal_Dependencies)
- [Virtual assistant](https://en.wikipedia.org/wiki/Virtual_assistant)
- [Voice user interface](https://en.wikipedia.org/wiki/Voice_user_interface)
- [Wikidata](https://en.wikipedia.org/wiki/Wikidata)
- [Word](https://en.wikipedia.org/wiki/Word)
- [Word-sense disambiguation](https://en.wikipedia.org/wiki/Word-sense_disambiguation)
- [Word-sense induction](https://en.wikipedia.org/wiki/Word-sense_induction)
- [Word2vec](https://en.wikipedia.org/wiki/Word2vec)
- [WordNet](https://en.wikipedia.org/wiki/WordNet)
- [Word embedding](https://en.wikipedia.org/wiki/Word_embedding)
- [Template:Natural language processing](https://en.wikipedia.org/wiki/Template:Natural_language_processing)
- [Template talk:Natural language processing](https://en.wikipedia.org/wiki/Template_talk:Natural_language_processing)
- [Help:IPA/English](https://en.wikipedia.org/wiki/Help:IPA/English)
- [Help:Pronunciation respelling key](https://en.wikipedia.org/wiki/Help:Pronunciation_respelling_key)

---
_This article is part of the Python Programming Language wiki archive._
_Retrieved and archived on: 2024-12-15T04:08:25.137134+00:00_