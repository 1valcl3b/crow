#!/bin/bash

case "$1" in
    --start)
        echo "=================================="
        echo " Iniciando Crow"
        echo "=================================="
        rm -f logs/*
        docker compose up -d --build > /dev/null
        echo
        echo "Crow iniciado."
        echo "Acesse a interface WEB: http://localhost:5000"
        ;;
    --destroy)
        echo "=================================="
        echo " Finalizando Crow"
        echo "=================================="
        docker compose down --rmi all 
        rm -f logs/*
        echo
        echo "Crow finalizado."
        ;;
    --restart)
        echo "=================================="
        echo " Reiniciando Crow"
        echo "=================================="
        docker compose down
        docker compose up -d --build
        ;;
    --logs)
        docker logs -f crow
        ;;
    *)
        echo
        echo "Uso:"
        echo
        echo "  ./crow.sh --start (Iniciar o Crow)"
        echo "  ./crow.sh --destroy (Parar e limpar os Logs)"
        echo "  ./crow.sh --restart (Reinicar o Crow)"
        echo "  ./crow.sh --logs (Visualizar Logs)"
        echo
        ;;
esac
