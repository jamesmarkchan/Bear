// Copyright Epic Games, Inc. All Rights Reserved.


#include "BearGameModeBase.h"

void ABearGameModeBase::BeginPlay()
{
    // VERY IMPORTANT: Always call the parent's BeginPlay first
    Super::BeginPlay();

    // Your logging code here:
    UE_LOG(LogTemp, Warning, TEXT("Bear project is alive and logging!"));
}

void ABearGameModeBase::StartPlay()
{
    // VERY IMPORTANT: Always call the parent's BeginPlay first
    Super::StartPlay();

    // Your logging code here:
    UE_LOG(LogTemp, Warning, TEXT("Bear is starting..."));
}