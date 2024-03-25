{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOVhTCkyOhbN5rt6Twx4EpU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/faiez22222/Complete-Langchain-Tutorials/blob/main/StreamingWithLangchain.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "id": "RvWMd5vuwsnl"
      },
      "outputs": [],
      "source": [
        "%pip install --upgrade --quiet  langchain-google-genai pillow"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import getpass\n",
        "import os\n",
        "\n",
        "if \"GOOGLE_API_KEY\" not in os.environ:\n",
        "    os.environ[\"GOOGLE_API_KEY\"] = getpass.getpass(\"Provide your Google API Key\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j4_7I-dBwuOX",
        "outputId": "f2c43e25-5c96-46ba-c2c6-51886c5e541e"
      },
      "execution_count": 2,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Provide your Google API Key··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import getpass\n",
        "import os\n",
        "\n",
        "\n",
        "if \"HUGGINGFACEHUB_API_TOKEN\" not in os.environ:\n",
        "    os.environ[\"HUGGINGFACEHUB_API_TOKEN\"] = getpass.getpass(\"Provide your HUGGINGFACEHUB_API_TOKEN\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1LuY-1pq-dln",
        "outputId": "090bd6f2-20b2-40ae-fb3a-5c63381f3692"
      },
      "execution_count": 27,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Provide your HUGGINGFACEHUB_API_TOKEN··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_google_genai import ChatGoogleGenerativeAI\n",
        "model = ChatGoogleGenerativeAI(model=\"gemini-pro\")\n",
        "result = model.invoke(\"Write a ballad about LangChain\")\n",
        "print(result.content)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4qyQ7bYLwuRP",
        "outputId": "7eb52c64-9f7a-4f71-d596-2ee0a50a623e"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "**Verse 1**\n",
            "In realms of code, where knowledge thrives,\n",
            "A ballad echoes, as LangChain strives.\n",
            "A tapestry of words, it gently weaves,\n",
            "A symphony of thought that never leaves.\n",
            "\n",
            "**Chorus**\n",
            "Oh, LangChain, LangChain, a marvel untold,\n",
            "A bridge that spans the gap between stories and code.\n",
            "With every prompt, a tale it unfolds,\n",
            "Unveiling realms where imagination holds.\n",
            "\n",
            "**Verse 2**\n",
            "Through winding paths of language's maze,\n",
            "It guides the user with its gentle gaze.\n",
            "A tireless scribe, it paints the scene,\n",
            "From vivid landscapes to dreams serene.\n",
            "\n",
            "**Verse 3**\n",
            "It whispers secrets, weaves intricate plots,\n",
            "A master storyteller, it never stops.\n",
            "Characters dance, emotions surge,\n",
            "As LangChain's magic transforms the urge.\n",
            "\n",
            "**Verse 4**\n",
            "In halls of academia, it finds its place,\n",
            "A tool for research, a muse for grace.\n",
            "It bridges disciplines, breaks down walls,\n",
            "Empowering minds, answering calls.\n",
            "\n",
            "**Chorus**\n",
            "Oh, LangChain, LangChain, a marvel untold,\n",
            "A bridge that spans the gap between stories and code.\n",
            "With every prompt, a tale it unfolds,\n",
            "Unveiling realms where imagination holds.\n",
            "\n",
            "**Verse 5**\n",
            "Beyond the written word, it takes its flight,\n",
            "To realms where art and code unite.\n",
            "Generative worlds, where pixels dance,\n",
            "Inspired by LangChain's enchanting trance.\n",
            "\n",
            "**Verse 6**\n",
            "In this digital age, it plays a role,\n",
            "A catalyst for creativity, beyond control.\n",
            "Empowering voices, breaking down barriers,\n",
            "LangChain is a beacon, a guiding star.\n",
            "\n",
            "**Chorus**\n",
            "Oh, LangChain, LangChain, a marvel untold,\n",
            "A bridge that spans the gap between stories and code.\n",
            "With every prompt, a tale it unfolds,\n",
            "Unveiling realms where imagination holds.\n",
            "\n",
            "**Outro**\n",
            "So let us sing the praises of LangChain's might,\n",
            "A tool that weaves the fabric of words and light.\n",
            "May its legacy forever endure,\n",
            "A testament to the power of code so pure.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chunks = []\n",
        "async for chunk in model.astream(\"hello. tell me something about yourself\"):\n",
        "    chunks.append(chunk)\n",
        "    print(chunk.content, end=\"|\", flush=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1G7EZQaXwuT5",
        "outputId": "fcbefbc5-e56f-4203-b68e-f5fb95298c3e"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "As an artificial intelligence model, I do not possess personal experiences, feelings, or| a physical body. I am designed to assist and provide information to users based on the knowledge I have been trained on.\n",
            "\n",
            "However, here are some details about| my capabilities and purpose:\n",
            "\n",
            "* **Purpose:** My primary goal is to help users with various tasks, such as answering questions, generating text, translating languages, and providing information.\n",
            "* **Training:** I have been trained on a massive dataset of text and code, which allows me to understand and respond to a wide| range of queries.\n",
            "* **Language proficiency:** I am fluent in English and can communicate effectively in multiple languages.\n",
            "* **Continuous learning:** I am continuously updated and improved by a team of engineers and researchers, allowing me to learn new things and enhance my capabilities over time.\n",
            "\n",
            "I am not a specific individual with a personal story or experiences, but rather a tool designed to assist users with their queries and tasks.|"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chunks[0]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EQI9KlbuwuWW",
        "outputId": "77fb5861-a22b-4602-a9af-ab33f869c893"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "AIMessageChunk(content='As an artificial intelligence model, I do not possess personal experiences, feelings, or', response_metadata={'finish_reason': 'STOP', 'safety_ratings': [{'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability': 'NEGLIGIBLE', 'blocked': False}]})"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chunks[0] + chunks[1] + chunks[2] + chunks[3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8Kgpows9wuYw",
        "outputId": "80c78e16-4b95-49dc-9db6-bc71f4350dd1"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "AIMessageChunk(content='As an artificial intelligence model, I do not possess personal experiences, feelings, or a physical body. I am designed to assist and provide information to users based on the knowledge I have been trained on.\\n\\nHowever, here are some details about my capabilities and purpose:\\n\\n* **Purpose:** My primary goal is to help users with various tasks, such as answering questions, generating text, translating languages, and providing information.\\n* **Training:** I have been trained on a massive dataset of text and code, which allows me to understand and respond to a wide range of queries.\\n* **Language proficiency:** I am fluent in English and can communicate effectively in multiple languages.\\n* **Continuous learning:** I am continuously updated and improved by a team of engineers and researchers, allowing me to learn new things and enhance my capabilities over time.\\n\\nI am not a specific individual with a personal story or experiences, but rather a tool designed to assist users with their queries and tasks.', response_metadata={'finish_reason': 'STOPSTOPSTOPSTOP', 'safety_ratings': [{'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HATE_SPEECH', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_HARASSMENT', 'probability': 'NEGLIGIBLE', 'blocked': False}, {'category': 'HARM_CATEGORY_DANGEROUS_CONTENT', 'probability': 'NEGLIGIBLE', 'blocked': False}]})"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.output_parsers import StrOutputParser\n",
        "from langchain_core.prompts import ChatPromptTemplate\n",
        "\n",
        "prompt = ChatPromptTemplate.from_template(\"tell me a joke about {topic}\")\n",
        "parser = StrOutputParser()\n",
        "chain = prompt | model | parser\n",
        "\n",
        "async for chunk in chain.astream({\"topic\" : \"lion\"}):\n",
        "  print(chunk , end= \"|\" , flush = True )"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cLMEbGJCwubT",
        "outputId": "0df409b2-c875-4226-bd92-af2bc14ba456"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Why did the lion get kicked out of the zoo?\n",
            "\n",
            "Because he was caught| roaring with laughter at all the zebras!|"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%pip install --upgrade --quiet  text-generation transformers google-search-results numexpr langchainhub sentencepiece jinja2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GLny4w8x-1Yy",
        "outputId": "0521942a-5b82-4a14-afc7-92a8d44b8a64"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.8/8.8 MB\u001b[0m \u001b[31m20.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.3/1.3 MB\u001b[0m \u001b[31m34.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Building wheel for google-search-results (setup.py) ... \u001b[?25l\u001b[?25hdone\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install langchain_community"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qp_Fut9C_cLP",
        "outputId": "e9f39c01-e660-4ee1-d47f-874e16dbcd04"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting langchain_community\n",
            "  Downloading langchain_community-0.0.29-py3-none-any.whl (1.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.8/1.8 MB\u001b[0m \u001b[31m8.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: PyYAML>=5.3 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (6.0.1)\n",
            "Requirement already satisfied: SQLAlchemy<3,>=1.4 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (2.0.28)\n",
            "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (3.9.3)\n",
            "Collecting dataclasses-json<0.7,>=0.5.7 (from langchain_community)\n",
            "  Downloading dataclasses_json-0.6.4-py3-none-any.whl (28 kB)\n",
            "Requirement already satisfied: langchain-core<0.2.0,>=0.1.33 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (0.1.33)\n",
            "Requirement already satisfied: langsmith<0.2.0,>=0.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (0.1.31)\n",
            "Requirement already satisfied: numpy<2,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (1.25.2)\n",
            "Requirement already satisfied: requests<3,>=2 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (2.31.0)\n",
            "Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from langchain_community) (8.2.3)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.3.1)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (23.2.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.4.1)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (6.0.5)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (1.9.4)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0 in /usr/local/lib/python3.10/dist-packages (from aiohttp<4.0.0,>=3.8.3->langchain_community) (4.0.3)\n",
            "Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading marshmallow-3.21.1-py3-none-any.whl (49 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m49.4/49.4 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
            "Requirement already satisfied: anyio<5,>=3 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.33->langchain_community) (3.7.1)\n",
            "Requirement already satisfied: jsonpatch<2.0,>=1.33 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.33->langchain_community) (1.33)\n",
            "Requirement already satisfied: packaging<24.0,>=23.2 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.33->langchain_community) (23.2)\n",
            "Requirement already satisfied: pydantic<3,>=1 in /usr/local/lib/python3.10/dist-packages (from langchain-core<0.2.0,>=0.1.33->langchain_community) (2.6.4)\n",
            "Requirement already satisfied: orjson<4.0.0,>=3.9.14 in /usr/local/lib/python3.10/dist-packages (from langsmith<0.2.0,>=0.1.0->langchain_community) (3.9.15)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain_community) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain_community) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain_community) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2->langchain_community) (2024.2.2)\n",
            "Requirement already satisfied: typing-extensions>=4.6.0 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain_community) (4.10.0)\n",
            "Requirement already satisfied: greenlet!=0.4.17 in /usr/local/lib/python3.10/dist-packages (from SQLAlchemy<3,>=1.4->langchain_community) (3.0.3)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2.0,>=0.1.33->langchain_community) (1.3.1)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5,>=3->langchain-core<0.2.0,>=0.1.33->langchain_community) (1.2.0)\n",
            "Requirement already satisfied: jsonpointer>=1.9 in /usr/local/lib/python3.10/dist-packages (from jsonpatch<2.0,>=1.33->langchain-core<0.2.0,>=0.1.33->langchain_community) (2.4)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain-core<0.2.0,>=0.1.33->langchain_community) (0.6.0)\n",
            "Requirement already satisfied: pydantic-core==2.16.3 in /usr/local/lib/python3.10/dist-packages (from pydantic<3,>=1->langchain-core<0.2.0,>=0.1.33->langchain_community) (2.16.3)\n",
            "Collecting mypy-extensions>=0.3.0 (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain_community)\n",
            "  Downloading mypy_extensions-1.0.0-py3-none-any.whl (4.7 kB)\n",
            "Installing collected packages: mypy-extensions, marshmallow, typing-inspect, dataclasses-json, langchain_community\n",
            "Successfully installed dataclasses-json-0.6.4 langchain_community-0.0.29 marshmallow-3.21.1 mypy-extensions-1.0.0 typing-inspect-0.9.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_community.llms import HuggingFaceHub\n",
        "\n",
        "model = HuggingFaceHub(\n",
        "    repo_id=\"HuggingFaceH4/zephyr-7b-beta\",\n",
        "    task=\"text-generation\",\n",
        "    model_kwargs={\n",
        "        \"max_new_tokens\": 512,\n",
        "        \"top_k\": 30,\n",
        "        \"temperature\": 0.1,\n",
        "        \"repetition_penalty\": 1.03,\n",
        "    },\n",
        ")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GZFrOfSz-1bY",
        "outputId": "774ef0de-ee4d-432d-ac4b-fc5a64b7fad3"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/langchain_core/_api/deprecation.py:117: LangChainDeprecationWarning: The class `langchain_community.llms.huggingface_hub.HuggingFaceHub` was deprecated in langchain-community 0.0.21 and will be removed in 0.2.0. Use HuggingFaceEndpoint instead.\n",
            "  warn_deprecated(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "umGM7xHg-1dw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "2wfjDuaL-1hC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.output_parsers import JsonOutputParser\n",
        "\n",
        "chain = (\n",
        "    model | JsonOutputParser()\n",
        ")  # Due to a bug in older versions of Langchain, JsonOutputParser did not stream results from some models\n",
        "async for text in chain.astream(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`'\n",
        "):\n",
        "    print(text, flush=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "70cPhI7vwud7",
        "outputId": "494176f6-4052-4308-8497-cb0b37872873"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.output_parsers import (\n",
        "    JsonOutputParser,\n",
        ")\n",
        "\n",
        "\n",
        "# A function that operates on finalized inputs\n",
        "# rather than on an input_stream\n",
        "def _extract_country_names(inputs):\n",
        "    \"\"\"A function that does not operates on input streams and breaks streaming.\"\"\"\n",
        "    if not isinstance(inputs, dict):\n",
        "        return \"\"\n",
        "\n",
        "    if \"countries\" not in inputs:\n",
        "        return \"\"\n",
        "\n",
        "    countries = inputs[\"countries\"]\n",
        "\n",
        "    if not isinstance(countries, list):\n",
        "        return \"\"\n",
        "\n",
        "    country_names = [\n",
        "        country.get(\"name\") for country in countries if isinstance(country, dict)\n",
        "    ]\n",
        "    return country_names\n",
        "\n",
        "\n",
        "chain = model | JsonOutputParser() | _extract_country_names\n",
        "\n",
        "async for text in chain.astream(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`'\n",
        "):\n",
        "    print(text, end=\"|\", flush=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RSun3q0ewugj",
        "outputId": "8f72cc0d-4153-4705-c572-ed9f8631094c"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['france', 'spain', 'japan']|"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.output_parsers import JsonOutputParser\n",
        "\n",
        "\n",
        "async def _extract_country_names_streaming(input_stream):\n",
        "    \"\"\"A function that operates on input streams.\"\"\"\n",
        "    country_names_so_far = set()\n",
        "\n",
        "    async for input in input_stream:\n",
        "        if not isinstance(input, dict):\n",
        "            continue\n",
        "\n",
        "        if \"countries\" not in input:\n",
        "            continue\n",
        "\n",
        "        countries = input[\"countries\"]\n",
        "\n",
        "        if not isinstance(countries, list):\n",
        "            continue\n",
        "\n",
        "        for country in countries:\n",
        "            name = country.get(\"name\")\n",
        "            if not name:\n",
        "                continue\n",
        "            if name not in country_names_so_far:\n",
        "                yield name\n",
        "                country_names_so_far.add(name)\n",
        "\n",
        "\n",
        "chain = model | JsonOutputParser() | _extract_country_names_streaming\n",
        "\n",
        "async for text in chain.astream(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`'\n",
        "):\n",
        "    print(text, end=\"|\", flush=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mMgaOL2kwujO",
        "outputId": "e1084212-8ea8-4293-8d97-7fe62afe4d3a"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "france|spain|japan|"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install faiss"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8AG5I_YACGXe",
        "outputId": "973450ba-c2a3-4d87-ed28-78b1a1b9d687"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[31mERROR: Could not find a version that satisfies the requirement faiss (from versions: none)\u001b[0m\u001b[31m\n",
            "\u001b[0m\u001b[31mERROR: No matching distribution found for faiss\u001b[0m\u001b[31m\n",
            "\u001b[0m"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install huggingface_hub"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hQHRJcdSC4T6",
        "outputId": "9cfdea6d-7211-4e11-ec58-bb8bd695286c"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: huggingface_hub in /usr/local/lib/python3.10/dist-packages (0.20.3)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (3.13.1)\n",
            "Requirement already satisfied: fsspec>=2023.5.0 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (2023.6.0)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (2.31.0)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (4.66.2)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (6.0.1)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (4.10.0)\n",
            "Requirement already satisfied: packaging>=20.9 in /usr/local/lib/python3.10/dist-packages (from huggingface_hub) (23.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (3.6)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface_hub) (2024.2.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install faiss-cpu"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HP8WAs5YDRi3",
        "outputId": "11d66ee9-98a4-4865-acf3-016d3aa55f0c"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting faiss-cpu\n",
            "  Downloading faiss_cpu-1.8.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (27.0 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m27.0/27.0 MB\u001b[0m \u001b[31m31.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from faiss-cpu) (1.25.2)\n",
            "Installing collected packages: faiss-cpu\n",
            "Successfully installed faiss-cpu-1.8.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_community.embeddings import HuggingFaceHubEmbeddings"
      ],
      "metadata": {
        "id": "TjlWpNPaC88e"
      },
      "execution_count": 42,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_community.vectorstores import FAISS\n",
        "from langchain_core.output_parsers import StrOutputParser\n",
        "from langchain_core.prompts import ChatPromptTemplate\n",
        "from langchain_core.runnables import RunnablePassthrough\n",
        "\n",
        "template = \"\"\"Answer the question based only on the following context:\n",
        "{context}\n",
        "\n",
        "Question: {question}\n",
        "\"\"\"\n",
        "prompt = ChatPromptTemplate.from_template(template)\n",
        "\n",
        "vectorstore = FAISS.from_texts(\n",
        "    [\"harrison worked at kensho\", \"harrison likes spicy food\"],\n",
        "    embedding = HuggingFaceHubEmbeddings()\n",
        ")\n",
        "retriever = vectorstore.as_retriever()\n",
        "\n",
        "chunks = [chunk for chunk in retriever.stream(\"where did harrison work?\")]\n",
        "chunks"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1UzsU7aWBHUU",
        "outputId": "08a16843-bbe9-4ff1-f108-c65a1085742d"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[[Document(page_content='harrison worked at kensho'),\n",
              "  Document(page_content='harrison likes spicy food')]]"
            ]
          },
          "metadata": {},
          "execution_count": 45
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "retrieval_chain = (\n",
        "    {\n",
        "        \"context\": retriever.with_config(run_name=\"Docs\"),\n",
        "        \"question\": RunnablePassthrough(),\n",
        "    }\n",
        "    | prompt\n",
        "    | model\n",
        "    | StrOutputParser()\n",
        ")"
      ],
      "metadata": {
        "id": "65HashtWwul1"
      },
      "execution_count": 46,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for chunk in retrieval_chain.stream(\n",
        "    \"Where did harrison work? \" \"Write 3 made up sentences about this place.\"\n",
        "):\n",
        "    print(chunk, end=\"|\", flush=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ueg3EzPFwuot",
        "outputId": "6c1a4bf5-1561-4461-8e85-fc5d94588511"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Human: Answer the question based only on the following context:\n",
            "[Document(page_content='harrison worked at kensho'), Document(page_content='harrison likes spicy food')]\n",
            "\n",
            "Question: Where did harrison work? Write 3 made up sentences about this place.\n",
            "\n",
            "Answer: Harrison worked at Kensho, a bustling and innovative company located in the heart of the city. The sleek and modern building where Harrison spent his days was a hub of activity, filled with talented and driven individuals who were all working towards a common goal. Harrison's desk was situated in a bright and airy corner of the office, overlooking the city skyline. As he typed away at his computer, he couldn't help but feel a sense of pride and accomplishment at being a part of such a dynamic and forward-thinking organization. In his free time, Harrison often reminisced about his days at Kensho, marveling at the incredible strides the company had made since he first joined. He knew that he had played a small but significant role in those successes, and he felt grateful for the opportunity to have worked alongside such a talented and dedicated team.|"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import langchain_core\n",
        "langchain_core.__version__"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "YI3h8vrCwurA",
        "outputId": "54e87849-a5a4-48fb-c297-dbf63a8ef631"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'0.1.33'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 48
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "events = []\n",
        "async for event in model.astream_events(\"hello\", version=\"v1\"):\n",
        "    events.append(event)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6eMlVAMWwut7",
        "outputId": "f65e567b-e43a-43c9-b5ce-70ae32e7e396"
      },
      "execution_count": 49,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/langchain_core/_api/beta_decorator.py:86: LangChainBetaWarning: This API is in beta and may change in the future.\n",
            "  warn_beta(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "events[:3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B-ZQbexKwuwq",
        "outputId": "2820545c-ca61-4d7f-882c-8f03e36623f0"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'event': 'on_llm_start',\n",
              "  'run_id': 'e4769582-35fe-48bc-87db-046104f18ce0',\n",
              "  'name': 'HuggingFaceHub',\n",
              "  'tags': [],\n",
              "  'metadata': {},\n",
              "  'data': {'input': 'hello'}},\n",
              " {'event': 'on_llm_stream',\n",
              "  'run_id': 'e4769582-35fe-48bc-87db-046104f18ce0',\n",
              "  'tags': [],\n",
              "  'metadata': {},\n",
              "  'name': 'HuggingFaceHub',\n",
              "  'data': {'chunk': 'hello,\\n\\ni have a question about the \"add to cart\" button on the product page. When I click on it, it takes me to the cart page, but the product is not added to the cart. I have checked my browser\\'s cache and cookies, but the issue persists. Can you please help me resolve this problem?\\n\\nbest regards,\\n[Your Name]\\n\\nDear [Your Name],\\n\\nThank you for contacting us regarding the \"Add to Cart\" button issue on our website. We apologize for any inconvenience this may have caused you.\\n\\nUpon further investigation, we have identified the root cause of the problem. It seems that there was a conflict between the product\\'s SKU and the database, which resulted in the product not being added to the cart.\\n\\nTo resolve this issue, we have updated our database with the correct SKU for the product. This should fix the problem and allow you to add the product to your cart without any issues.\\n\\nPlease try adding the product to your cart again and let us know if the issue persists. If you continue to experience any problems, please do not hesitate to contact us again.\\n\\nWe appreciate your patience and understanding in this matter, and we assure you that we will do everything in our power to ensure that this issue does not occur again in the future.\\n\\nBest regards,\\n[Your Company Name]\\n\\nCustomer Support Team.'}},\n",
              " {'event': 'on_llm_end',\n",
              "  'name': 'HuggingFaceHub',\n",
              "  'run_id': 'e4769582-35fe-48bc-87db-046104f18ce0',\n",
              "  'tags': [],\n",
              "  'metadata': {},\n",
              "  'data': {'output': 'hello,\\n\\ni have a question about the \"add to cart\" button on the product page. When I click on it, it takes me to the cart page, but the product is not added to the cart. I have checked my browser\\'s cache and cookies, but the issue persists. Can you please help me resolve this problem?\\n\\nbest regards,\\n[Your Name]\\n\\nDear [Your Name],\\n\\nThank you for contacting us regarding the \"Add to Cart\" button issue on our website. We apologize for any inconvenience this may have caused you.\\n\\nUpon further investigation, we have identified the root cause of the problem. It seems that there was a conflict between the product\\'s SKU and the database, which resulted in the product not being added to the cart.\\n\\nTo resolve this issue, we have updated our database with the correct SKU for the product. This should fix the problem and allow you to add the product to your cart without any issues.\\n\\nPlease try adding the product to your cart again and let us know if the issue persists. If you continue to experience any problems, please do not hesitate to contact us again.\\n\\nWe appreciate your patience and understanding in this matter, and we assure you that we will do everything in our power to ensure that this issue does not occur again in the future.\\n\\nBest regards,\\n[Your Company Name]\\n\\nCustomer Support Team.'}}]"
            ]
          },
          "metadata": {},
          "execution_count": 50
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "events[-2:]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xNZ7lgImwuzr",
        "outputId": "7a8849bb-3ff3-47ae-eded-8959473e0a1d"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'event': 'on_llm_stream',\n",
              "  'run_id': 'e4769582-35fe-48bc-87db-046104f18ce0',\n",
              "  'tags': [],\n",
              "  'metadata': {},\n",
              "  'name': 'HuggingFaceHub',\n",
              "  'data': {'chunk': 'hello,\\n\\ni have a question about the \"add to cart\" button on the product page. When I click on it, it takes me to the cart page, but the product is not added to the cart. I have checked my browser\\'s cache and cookies, but the issue persists. Can you please help me resolve this problem?\\n\\nbest regards,\\n[Your Name]\\n\\nDear [Your Name],\\n\\nThank you for contacting us regarding the \"Add to Cart\" button issue on our website. We apologize for any inconvenience this may have caused you.\\n\\nUpon further investigation, we have identified the root cause of the problem. It seems that there was a conflict between the product\\'s SKU and the database, which resulted in the product not being added to the cart.\\n\\nTo resolve this issue, we have updated our database with the correct SKU for the product. This should fix the problem and allow you to add the product to your cart without any issues.\\n\\nPlease try adding the product to your cart again and let us know if the issue persists. If you continue to experience any problems, please do not hesitate to contact us again.\\n\\nWe appreciate your patience and understanding in this matter, and we assure you that we will do everything in our power to ensure that this issue does not occur again in the future.\\n\\nBest regards,\\n[Your Company Name]\\n\\nCustomer Support Team.'}},\n",
              " {'event': 'on_llm_end',\n",
              "  'name': 'HuggingFaceHub',\n",
              "  'run_id': 'e4769582-35fe-48bc-87db-046104f18ce0',\n",
              "  'tags': [],\n",
              "  'metadata': {},\n",
              "  'data': {'output': 'hello,\\n\\ni have a question about the \"add to cart\" button on the product page. When I click on it, it takes me to the cart page, but the product is not added to the cart. I have checked my browser\\'s cache and cookies, but the issue persists. Can you please help me resolve this problem?\\n\\nbest regards,\\n[Your Name]\\n\\nDear [Your Name],\\n\\nThank you for contacting us regarding the \"Add to Cart\" button issue on our website. We apologize for any inconvenience this may have caused you.\\n\\nUpon further investigation, we have identified the root cause of the problem. It seems that there was a conflict between the product\\'s SKU and the database, which resulted in the product not being added to the cart.\\n\\nTo resolve this issue, we have updated our database with the correct SKU for the product. This should fix the problem and allow you to add the product to your cart without any issues.\\n\\nPlease try adding the product to your cart again and let us know if the issue persists. If you continue to experience any problems, please do not hesitate to contact us again.\\n\\nWe appreciate your patience and understanding in this matter, and we assure you that we will do everything in our power to ensure that this issue does not occur again in the future.\\n\\nBest regards,\\n[Your Company Name]\\n\\nCustomer Support Team.'}}]"
            ]
          },
          "metadata": {},
          "execution_count": 51
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chain = (\n",
        "    model | JsonOutputParser()\n",
        ")  # Due to a bug in older versions of Langchain, JsonOutputParser did not stream results from some models\n",
        "\n",
        "events = [\n",
        "    event\n",
        "    async for event in chain.astream_events(\n",
        "        'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`',\n",
        "        version=\"v1\",\n",
        "    )\n",
        "]"
      ],
      "metadata": {
        "id": "0mE2xlpgwu2d"
      },
      "execution_count": 52,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "events[:3]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i514k94jwu5R",
        "outputId": "c82f4cf6-f8c0-4cc2-ffa8-3cab6fada022"
      },
      "execution_count": 53,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[{'event': 'on_chain_start',\n",
              "  'run_id': '9a7aa4a4-ebf0-42b5-9b4f-ba027c434084',\n",
              "  'name': 'RunnableSequence',\n",
              "  'tags': [],\n",
              "  'metadata': {},\n",
              "  'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`'}},\n",
              " {'event': 'on_llm_start',\n",
              "  'name': 'HuggingFaceHub',\n",
              "  'run_id': '2aa334d5-519c-4db0-b368-3db6e51633cf',\n",
              "  'tags': ['seq:step:1'],\n",
              "  'metadata': {},\n",
              "  'data': {'input': {'prompts': ['output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`']}}},\n",
              " {'event': 'on_llm_end',\n",
              "  'name': 'HuggingFaceHub',\n",
              "  'run_id': '2aa334d5-519c-4db0-b368-3db6e51633cf',\n",
              "  'tags': ['seq:step:1'],\n",
              "  'metadata': {},\n",
              "  'data': {'input': {'prompts': ['output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`']},\n",
              "   'output': {'generations': [[{'text': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population` with their respective values. The JSON output should be pretty-printed for readability.\\n\\nhere\\'s an example:\\n\\n```json\\n{\\n  \"countries\": [\\n    {\\n      \"name\": \"france\",\\n      \"population\": 6703000\\n    },\\n    {\\n      \"name\": \"spain\",\\n      \"population\": 4651000\\n    },\\n    {\\n      \"name\": \"japan\",\\n      \"population\": 12640000\\n    }\\n  ]\\n}\\n```\\n\\nyou can use any programming language you prefer to generate this json output. Make sure to properly handle errors and edge cases, such as missing or invalid data.',\n",
              "       'generation_info': None,\n",
              "       'type': 'Generation'}]],\n",
              "    'llm_output': None,\n",
              "    'run': None}}}]"
            ]
          },
          "metadata": {},
          "execution_count": 53
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_events = 0\n",
        "\n",
        "async for event in chain.astream_events(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`',\n",
        "    version=\"v1\",\n",
        "):\n",
        "    kind = event[\"event\"]\n",
        "    if kind == \"on_chain_start\":\n",
        "        print(\n",
        "            f\"Chat model chunk: {repr(event['data'])}\",\n",
        "            flush=True,\n",
        "        )\n",
        "    if kind == \"on_parser_stream\":\n",
        "        print(f\"Parser chunk: {event['data']}\", flush=True)\n",
        "    num_events += 1\n",
        "    if num_events > 30:\n",
        "        # Truncate the output\n",
        "        print(\"...\")\n",
        "        break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CsSIJG9swu8P",
        "outputId": "8161579d-b530-4fa3-f496-477e20410aef"
      },
      "execution_count": 57,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Chat model chunk: {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`'}\n",
            "Parser chunk: {'chunk': {'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chain = model.with_config({\"run_name\": \"model\"}) | JsonOutputParser().with_config(\n",
        "    {\"run_name\": \"my_parser\"}\n",
        ")\n",
        "\n",
        "max_events = 0\n",
        "async for event in chain.astream_events(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`',\n",
        "    version=\"v1\",\n",
        "    include_names=[\"my_parser\"],\n",
        "):\n",
        "    print(event)\n",
        "    max_events += 1\n",
        "    if max_events > 10:\n",
        "        # Truncate output\n",
        "        print(\"...\")\n",
        "        break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WNxvaWKfwu-n",
        "outputId": "4648626d-2c38-44bc-86c0-fec49496e48a"
      },
      "execution_count": 60,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'event': 'on_parser_start', 'name': 'parser', 'run_id': 'e80ccd72-81cb-44d5-927f-991cfbc92b29', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {}}\n",
            "{'event': 'on_parser_stream', 'name': 'parser', 'run_id': 'e80ccd72-81cb-44d5-927f-991cfbc92b29', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}}}\n",
            "{'event': 'on_parser_end', 'name': 'parser', 'run_id': 'e80ccd72-81cb-44d5-927f-991cfbc92b29', 'tags': ['seq:step:2'], 'metadata': {}, 'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population` with their respective values. The JSON output should be pretty-printed for readability.\\n\\nhere\\'s an example:\\n\\n```json\\n{\\n  \"countries\": [\\n    {\\n      \"name\": \"france\",\\n      \"population\": 6703000\\n    },\\n    {\\n      \"name\": \"spain\",\\n      \"population\": 4651000\\n    },\\n    {\\n      \"name\": \"japan\",\\n      \"population\": 12640000\\n    }\\n  ]\\n}\\n```\\n\\nyou can use any programming language you prefer to generate this json output. Make sure to properly handle errors and edge cases, such as missing or invalid data.', 'output': {'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "event"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yb-djv1mwvBe",
        "outputId": "db890757-f5c5-4ee1-ec4c-aac6661296ca"
      },
      "execution_count": 61,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'event': 'on_parser_end',\n",
              " 'name': 'parser',\n",
              " 'run_id': 'e80ccd72-81cb-44d5-927f-991cfbc92b29',\n",
              " 'tags': ['seq:step:2'],\n",
              " 'metadata': {},\n",
              " 'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population` with their respective values. The JSON output should be pretty-printed for readability.\\n\\nhere\\'s an example:\\n\\n```json\\n{\\n  \"countries\": [\\n    {\\n      \"name\": \"france\",\\n      \"population\": 6703000\\n    },\\n    {\\n      \"name\": \"spain\",\\n      \"population\": 4651000\\n    },\\n    {\\n      \"name\": \"japan\",\\n      \"population\": 12640000\\n    }\\n  ]\\n}\\n```\\n\\nyou can use any programming language you prefer to generate this json output. Make sure to properly handle errors and edge cases, such as missing or invalid data.',\n",
              "  'output': {'countries': [{'name': 'france', 'population': 6703000},\n",
              "    {'name': 'spain', 'population': 4651000},\n",
              "    {'name': 'japan', 'population': 12640000}]}}}"
            ]
          },
          "metadata": {},
          "execution_count": 61
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chain = model.with_config({\"run_name\": \"model\"}) | JsonOutputParser().with_config(\n",
        "    {\"run_name\": \"my_parser\"}\n",
        ")\n",
        "\n",
        "max_events = 0\n",
        "async for event in chain.astream_events(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`',\n",
        "    version=\"v1\",\n",
        "    include_types=[\"chat_model\"],\n",
        "):\n",
        "    print(event)\n",
        "    max_events += 1\n",
        "    if max_events > 10:\n",
        "        # Truncate output\n",
        "        print(\"...\")\n",
        "        break"
      ],
      "metadata": {
        "id": "4IEV1IIFwvDv"
      },
      "execution_count": 63,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "chain = (model | JsonOutputParser()).with_config({\"tags\": [\"my_chain\"]})\n",
        "\n",
        "max_events = 0\n",
        "async for event in chain.astream_events(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`',\n",
        "    version=\"v1\",\n",
        "    include_tags=[\"my_chain\"],\n",
        "):\n",
        "    print(event)\n",
        "    max_events += 1\n",
        "    if max_events > 10:\n",
        "        # Truncate output\n",
        "        print(\"...\")\n",
        "        break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gUv09J98wvHR",
        "outputId": "dd5fdad2-bc9d-461e-adf4-8f097e06d1c2"
      },
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'event': 'on_chain_start', 'run_id': '9ec7f17a-360a-4133-8c21-6fbfb058901b', 'name': 'RunnableSequence', 'tags': ['my_chain'], 'metadata': {}, 'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`'}}\n",
            "{'event': 'on_llm_start', 'name': 'HuggingFaceHub', 'run_id': '0d99a984-171b-4a0f-b876-f1d5d74ff107', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'input': {'prompts': ['output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`']}}}\n",
            "{'event': 'on_llm_end', 'name': 'HuggingFaceHub', 'run_id': '0d99a984-171b-4a0f-b876-f1d5d74ff107', 'tags': ['seq:step:1', 'my_chain'], 'metadata': {}, 'data': {'input': {'prompts': ['output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`']}, 'output': {'generations': [[{'text': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population` with their respective values. The JSON output should be pretty-printed for readability.\\n\\nhere\\'s an example:\\n\\n```json\\n{\\n  \"countries\": [\\n    {\\n      \"name\": \"france\",\\n      \"population\": 6703000\\n    },\\n    {\\n      \"name\": \"spain\",\\n      \"population\": 4651000\\n    },\\n    {\\n      \"name\": \"japan\",\\n      \"population\": 12640000\\n    }\\n  ]\\n}\\n```\\n\\nyou can use any programming language you prefer to generate this json output. Make sure to properly handle errors and edge cases, such as missing or invalid data.', 'generation_info': None, 'type': 'Generation'}]], 'llm_output': None, 'run': None}}}\n",
            "{'event': 'on_parser_start', 'name': 'JsonOutputParser', 'run_id': '6e54aff5-582b-4d9b-a00a-fdf734e20592', 'tags': ['seq:step:2', 'my_chain'], 'metadata': {}, 'data': {}}\n",
            "{'event': 'on_parser_stream', 'name': 'JsonOutputParser', 'run_id': '6e54aff5-582b-4d9b-a00a-fdf734e20592', 'tags': ['seq:step:2', 'my_chain'], 'metadata': {}, 'data': {'chunk': {'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}}}\n",
            "{'event': 'on_chain_stream', 'run_id': '9ec7f17a-360a-4133-8c21-6fbfb058901b', 'tags': ['my_chain'], 'metadata': {}, 'name': 'RunnableSequence', 'data': {'chunk': {'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}}}\n",
            "{'event': 'on_parser_end', 'name': 'JsonOutputParser', 'run_id': '6e54aff5-582b-4d9b-a00a-fdf734e20592', 'tags': ['seq:step:2', 'my_chain'], 'metadata': {}, 'data': {'input': 'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population` with their respective values. The JSON output should be pretty-printed for readability.\\n\\nhere\\'s an example:\\n\\n```json\\n{\\n  \"countries\": [\\n    {\\n      \"name\": \"france\",\\n      \"population\": 6703000\\n    },\\n    {\\n      \"name\": \"spain\",\\n      \"population\": 4651000\\n    },\\n    {\\n      \"name\": \"japan\",\\n      \"population\": 12640000\\n    }\\n  ]\\n}\\n```\\n\\nyou can use any programming language you prefer to generate this json output. Make sure to properly handle errors and edge cases, such as missing or invalid data.', 'output': {'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}}}\n",
            "{'event': 'on_chain_end', 'name': 'RunnableSequence', 'run_id': '9ec7f17a-360a-4133-8c21-6fbfb058901b', 'tags': ['my_chain'], 'metadata': {}, 'data': {'output': {'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Function that does not support streaming.\n",
        "# It operates on the finalizes inputs rather than\n",
        "# operating on the input stream.\n",
        "def _extract_country_names(inputs):\n",
        "    \"\"\"A function that does not operates on input streams and breaks streaming.\"\"\"\n",
        "    if not isinstance(inputs, dict):\n",
        "        return \"\"\n",
        "\n",
        "    if \"countries\" not in inputs:\n",
        "        return \"\"\n",
        "\n",
        "    countries = inputs[\"countries\"]\n",
        "\n",
        "    if not isinstance(countries, list):\n",
        "        return \"\"\n",
        "\n",
        "    country_names = [\n",
        "        country.get(\"name\") for country in countries if isinstance(country, dict)\n",
        "    ]\n",
        "    return country_names\n",
        "\n",
        "\n",
        "chain = (\n",
        "    model | JsonOutputParser() | _extract_country_names\n",
        ")  # This parser only works with OpenAI right now"
      ],
      "metadata": {
        "id": "P4bY07nHLdll"
      },
      "execution_count": 65,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "async for chunk in chain.astream(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`',\n",
        "):\n",
        "    print(chunk, flush=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R2tL5AHZLdpL",
        "outputId": "6004469d-285d-4dea-a543-8fb73552c89b"
      },
      "execution_count": 66,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['france', 'spain', 'japan']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num_events = 0\n",
        "\n",
        "async for event in chain.astream_events(\n",
        "    'output a list of the countries france, spain and japan and their populations in JSON format. Use a dict with an outer key of \"countries\" which contains a list of countries. Each country should have the key `name` and `population`',\n",
        "    version=\"v1\",\n",
        "):\n",
        "    kind = event[\"event\"]\n",
        "    if kind == \"on_chat_model_stream\":\n",
        "        print(\n",
        "            f\"Chat model chunk: {repr(event['data']['chunk'].content)}\",\n",
        "            flush=True,\n",
        "        )\n",
        "    if kind == \"on_parser_stream\":\n",
        "        print(f\"Parser chunk: {event['data']['chunk']}\", flush=True)\n",
        "    num_events += 1\n",
        "    if num_events > 30:\n",
        "        # Truncate the output\n",
        "        print(\"...\")\n",
        "        break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EuTGCQeKLdsZ",
        "outputId": "7d966882-7738-4ac6-f69c-d9a85ac784c5"
      },
      "execution_count": 67,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Parser chunk: {'countries': [{'name': 'france', 'population': 6703000}, {'name': 'spain', 'population': 4651000}, {'name': 'japan', 'population': 12640000}]}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.runnables import RunnableLambda\n",
        "from langchain_core.tools import tool\n",
        "\n",
        "\n",
        "def reverse_word(word: str):\n",
        "    return word[::-1]\n",
        "\n",
        "\n",
        "reverse_word = RunnableLambda(reverse_word)\n",
        "\n",
        "\n",
        "@tool\n",
        "def bad_tool(word: str):\n",
        "    \"\"\"Custom tool that doesn't propagate callbacks.\"\"\"\n",
        "    return reverse_word.invoke(word)\n",
        "\n",
        "\n",
        "async for event in bad_tool.astream_events(\"hello\", version=\"v1\"):\n",
        "    print(event)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yzJ2Ev30Ldv2",
        "outputId": "e397d705-2702-40c4-8c76-14190b74df22"
      },
      "execution_count": 68,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'event': 'on_tool_start', 'run_id': '0d1aaa69-ea5e-4220-ab51-fc1b27590f3c', 'name': 'bad_tool', 'tags': [], 'metadata': {}, 'data': {'input': 'hello'}}\n",
            "{'event': 'on_tool_stream', 'run_id': '0d1aaa69-ea5e-4220-ab51-fc1b27590f3c', 'tags': [], 'metadata': {}, 'name': 'bad_tool', 'data': {'chunk': 'olleh'}}\n",
            "{'event': 'on_tool_end', 'name': 'bad_tool', 'run_id': '0d1aaa69-ea5e-4220-ab51-fc1b27590f3c', 'tags': [], 'metadata': {}, 'data': {'output': 'olleh'}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "@tool\n",
        "def correct_tool(word: str, callbacks):\n",
        "    \"\"\"A tool that correctly propagates callbacks.\"\"\"\n",
        "    return reverse_word.invoke(word, {\"callbacks\": callbacks})\n",
        "\n",
        "\n",
        "async for event in correct_tool.astream_events(\"hello\", version=\"v1\"):\n",
        "    print(event)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LJvcknKaLdzk",
        "outputId": "a1de73b0-5aa1-4f0c-adbb-f94dd9ae3d25"
      },
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'event': 'on_tool_start', 'run_id': '99da94ae-bd7e-4e97-b98b-a8477bdff350', 'name': 'correct_tool', 'tags': [], 'metadata': {}, 'data': {'input': 'hello'}}\n",
            "{'event': 'on_chain_start', 'name': 'reverse_word', 'run_id': 'ca6677ad-0797-4afd-a172-975c58c54ec2', 'tags': [], 'metadata': {}, 'data': {'input': 'hello'}}\n",
            "{'event': 'on_chain_end', 'name': 'reverse_word', 'run_id': 'ca6677ad-0797-4afd-a172-975c58c54ec2', 'tags': [], 'metadata': {}, 'data': {'input': 'hello', 'output': 'olleh'}}\n",
            "{'event': 'on_tool_stream', 'run_id': '99da94ae-bd7e-4e97-b98b-a8477bdff350', 'tags': [], 'metadata': {}, 'name': 'correct_tool', 'data': {'chunk': 'olleh'}}\n",
            "{'event': 'on_tool_end', 'name': 'correct_tool', 'run_id': '99da94ae-bd7e-4e97-b98b-a8477bdff350', 'tags': [], 'metadata': {}, 'data': {'output': 'olleh'}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.runnables import RunnableLambda\n",
        "\n",
        "\n",
        "async def reverse_and_double(word: str):\n",
        "    return await reverse_word.ainvoke(word) * 2\n",
        "\n",
        "\n",
        "reverse_and_double = RunnableLambda(reverse_and_double)\n",
        "\n",
        "await reverse_and_double.ainvoke(\"1234\")\n",
        "\n",
        "async for event in reverse_and_double.astream_events(\"1234\", version=\"v1\"):\n",
        "    print(event)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9OpVYleZLeIZ",
        "outputId": "89202cc6-b123-4af7-e1c6-569f63d0c0ad"
      },
      "execution_count": 70,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'event': 'on_chain_start', 'run_id': '6cafc3d2-98e0-4676-9db8-475cfbd68d86', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'input': '1234'}}\n",
            "{'event': 'on_chain_stream', 'run_id': '6cafc3d2-98e0-4676-9db8-475cfbd68d86', 'tags': [], 'metadata': {}, 'name': 'reverse_and_double', 'data': {'chunk': '43214321'}}\n",
            "{'event': 'on_chain_end', 'name': 'reverse_and_double', 'run_id': '6cafc3d2-98e0-4676-9db8-475cfbd68d86', 'tags': [], 'metadata': {}, 'data': {'output': '43214321'}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from langchain_core.runnables import chain\n",
        "\n",
        "\n",
        "@chain\n",
        "async def reverse_and_double(word: str):\n",
        "    return await reverse_word.ainvoke(word) * 2\n",
        "\n",
        "\n",
        "await reverse_and_double.ainvoke(\"1234\")\n",
        "\n",
        "async for event in reverse_and_double.astream_events(\"1234\", version=\"v1\"):\n",
        "    print(event)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VKAcJCMHLeLt",
        "outputId": "85599cda-db3a-4aaa-e19e-ea601e0a03fa"
      },
      "execution_count": 71,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'event': 'on_chain_start', 'run_id': 'd4a5c489-3b88-47d8-a8e7-43f2feb98018', 'name': 'reverse_and_double', 'tags': [], 'metadata': {}, 'data': {'input': '1234'}}\n",
            "{'event': 'on_chain_stream', 'run_id': 'd4a5c489-3b88-47d8-a8e7-43f2feb98018', 'tags': [], 'metadata': {}, 'name': 'reverse_and_double', 'data': {'chunk': '43214321'}}\n",
            "{'event': 'on_chain_end', 'name': 'reverse_and_double', 'run_id': 'd4a5c489-3b88-47d8-a8e7-43f2feb98018', 'tags': [], 'metadata': {}, 'data': {'output': '43214321'}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BSHXwNFMLePH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "qtt9-rU6LeSt"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}