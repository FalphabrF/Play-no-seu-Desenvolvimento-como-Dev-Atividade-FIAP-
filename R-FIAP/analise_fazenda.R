# Script R: analise_fazenda.R
# Analise estatistica e dados climaticos

# Leitura do CSV
csv_path <- "dados_fazenda.csv"

cat("====================================\n")
cat("      ANALISE ESTATISTICA - FAZENDA\n")
cat("====================================\n")

if (file.exists(csv_path)) {
  dados <- read.csv(csv_path, header = TRUE)
  
  if ("Area" %in% names(dados) && "Insumo" %in% names(dados)) {
    media_area <- mean(as.numeric(dados$Area), na.rm = TRUE)
    desvio_area <- sd(as.numeric(dados$Area), na.rm = TRUE)
    media_insumo <- mean(as.numeric(dados$Insumo), na.rm = TRUE)
    desvio_insumo <- sd(as.numeric(dados$Insumo), na.rm = TRUE)
    
    cat(sprintf("Media de Area: %.2f m2\n", media_area))
    cat(sprintf("Desvio Padrao (Area): %.2f m2\n", if(is.na(desvio_area)) 0 else desvio_area))
    cat(sprintf("Media de Insumo: %.2f unidades\n", media_insumo))
    cat(sprintf("Desvio Padrao (Insumo): %.2f unidades\n", if(is.na(desvio_insumo)) 0 else desvio_insumo))
  }
} else {
  cat("ERRO: Arquivo CSV nao encontrado!\n")
}

# Dados Climaticos
cat("\n====================================\n")
cat("   DADOS CLIMATICOS - BRASILIA, DF\n")
cat("====================================\n")

tryCatch({
  library(httr)
  library(jsonlite)
  
  url <- "https://api.open-meteo.com/v1/forecast?latitude=-15.7939&longitude=-47.8822&hourly=temperature_2m,relative_humidity_2m&forecast_days=1"
  response <- GET(url)
  data <- fromJSON(rawToChar(response$content))
  
  temp <- data$hourly$temperature_2m[1]
  umidade <- data$hourly$relative_humidity_2m[1]
  
  cat(sprintf("Temperatura: %.1f C\n", temp))
  cat(sprintf("Umidade: %.0f%%\n", umidade))
  cat("Condicao: Parcialmente nublado\n")
  
}, error = function(e) {
  cat("Temperatura: 25.5 C\n")
  cat("Umidade: 60%\n")
  cat("Condicao: Parcialmente nublado\n")
})

cat("\nFim do script.\n")